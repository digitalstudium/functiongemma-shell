#!/usr/bin/env python3
"""
Interactive chat mode with tool support.
"""

import json
import os
import subprocess
import time
import urllib.request
from pathlib import Path

from ollama import chat
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from transformers.utils import get_json_schema

console = Console()
# model = 'qwen3:1.7b'
model = "functiongemma"


def check_website(url: str) -> str:
    """
    Check website availability (HTTP status).

    Args:
        url: Website address (e.g., "google.com" or "https://github.com").

    Returns:
        A JSON string containing status code and latency information.
    """
    # Add protocol if missing
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        start_time = time.time()
        # 5 second timeout to avoid hanging
        with urllib.request.urlopen(url, timeout=5) as response:
            end_time = time.time()
            duration = end_time - start_time

            return json.dumps(
                {
                    "status": "success",
                    "url": url,
                    "code": response.getcode(),
                    "reason": response.reason,
                    "latency": f"{duration:.3f}s",
                },
                ensure_ascii=False,
            )

    except urllib.error.HTTPError as e:
        return json.dumps(
            {
                "status": "success",  # Request technically succeeded, just returned error code (404, 500, etc.)
                "url": url,
                "code": e.code,
                "reason": e.reason,
                "latency": "N/A",
            },
            ensure_ascii=False,
        )
    except Exception as e:
        return json.dumps(
            {"status": "error", "url": url, "message": str(e)}, ensure_ascii=False
        )


def find_largest_file(directory: str = ".") -> str:
    """
    Find the largest file in a directory using bash commands.

    Args:
        directory: Directory path to search in. Defaults to current directory.

    Returns:
        A JSON string with information about the largest file found.
    """
    try:
        directory = os.path.expandvars(directory)
        directory = os.path.expanduser(directory)

        bash_command = f"find {directory} -type f -exec du -h {{}} + 2>/dev/null | sort -rh | head -1"

        result = subprocess.run(
            bash_command, shell=True, capture_output=True, text=True, timeout=30
        )

        if result.returncode == 0 and result.stdout.strip():
            output = result.stdout.strip()
            parts = output.split("\t", 1)

            if len(parts) == 2:
                size, filepath = parts
                return json.dumps(
                    {
                        "status": "success",
                        "largest_file": filepath,
                        "size": size,
                        "directory": directory,
                    },
                    ensure_ascii=False,
                )
            else:
                return json.dumps(
                    {
                        "status": "error",
                        "message": "Failed to parse command output",
                    },
                    ensure_ascii=False,
                )
        else:
            return json.dumps(
                {"status": "error", "message": "No files found or access denied"},
                ensure_ascii=False,
            )

    except subprocess.TimeoutExpired:
        return json.dumps(
            {"status": "error", "message": "Timeout exceeded"},
            ensure_ascii=False,
        )
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)}, ensure_ascii=False)


def get_system_info() -> str:
    """
    Get basic system information: OS, kernel, memory, disk.

    Returns:
        JSON string with system information
    """
    try:
        info = {"status": "success"}

        # OS information
        try:
            # Try /etc/os-release (works on most Linux)
            if os.path.exists("/etc/os-release"):
                os_info = {}
                with open("/etc/os-release", "r") as f:
                    for line in f:
                        line = line.strip()
                        if "=" in line:
                            key, value = line.split("=", 1)
                            os_info[key] = value.strip('"')

                info["os_name"] = os_info.get("PRETTY_NAME") or os_info.get(
                    "NAME", "Unknown"
                )
                info["os_version"] = os_info.get("VERSION_ID", "")
            else:
                # Fallback: use uname
                result = subprocess.run(
                    ["uname", "-sr"], capture_output=True, text=True, timeout=5
                )
                if result.returncode == 0:
                    info["os_name"] = result.stdout.strip()
        except:
            info["os_name"] = "N/A"

        # Hostname
        try:
            result = subprocess.run(
                ["hostname"], capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                info["hostname"] = result.stdout.strip()
        except:
            pass

        # CPU cores
        try:
            info["cpu_cores"] = os.cpu_count()
        except:
            info["cpu_cores"] = "N/A"

        # Memory (free -h)
        try:
            result = subprocess.run(
                ["free", "-h"], capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")
                if len(lines) >= 2:
                    parts = lines[1].split()
                    if len(parts) >= 3:
                        info["memory_total"] = parts[1]
                        info["memory_used"] = parts[2]
                        info["memory_available"] = (
                            parts[6] if len(parts) > 6 else parts[3]
                        )
        except:
            info["memory"] = "N/A"

        # Disk (df -h /)
        try:
            result = subprocess.run(
                ["df", "-h", "/"], capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")
                if len(lines) >= 2:
                    parts = lines[1].split()
                    if len(parts) >= 4:
                        info["disk_total"] = parts[1]
                        info["disk_used"] = parts[2]
                        info["disk_free"] = parts[3]
        except:
            info["disk"] = "N/A"

        return json.dumps(info, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)}, ensure_ascii=False)


# 🎯 RESPONSE TEMPLATES
def format_tool_response(tool_name: str, arguments: dict, result_json: str) -> str:
    """
    Formats response based on tool name template.

    Args:
        tool_name: Name of the called tool
        arguments: Arguments the tool was called with
        result_json: JSON result from tool execution

    Returns:
        Formatted text for the user
    """
    try:
        result = json.loads(result_json)
    except:
        return f"❌ Error processing tool result {tool_name}"

    # Check for error
    if result.get("status") == "error":
        return f"❌ **Error:** {result.get('message', 'Unknown error')}"

    # Templates for different tools
    if tool_name == "find_largest_file":
        return f"""📁 **Largest file in directory `{result["directory"]}`:**

**File:** `{result["largest_file"]}`
**Size:** {result["size"]}
"""

    elif tool_name == "check_website":
        if result.get("status") == "error":
            return f"❌ **Connection error to `{result['url']}`:**\n{result.get('message')}"

        # Choose emoji based on response code
        code = result.get("code")
        icon = "✅" if code == 200 else "⚠️" if code < 500 else "🔥"

        return f"""🌐 **Check result for `{result["url"]}`:**

{icon} **Status:** {code} ({result.get("reason")})
⏱️ **Response time:** {result.get("latency")}
"""

    elif tool_name == "get_system_info":
        output = ["🖥️  **System Information:**\n"]

        # OS
        if "os_name" in result:
            os_str = result["os_name"]
            if result.get("os_version"):
                os_str += f" (version: {result['os_version']})"
            output.append(f"**OS:** {os_str}\n")

        # Host
        if "hostname" in result:
            output.append(f"**Host:** {result['hostname']}\n")

        # CPU
        if "cpu_cores" in result:
            output.append(f"**CPU Cores:** {result['cpu_cores']}\n")

        # Memory
        if "memory_total" in result:
            output.append(
                f"**Memory:** {result.get('memory_used', '?')} / {result['memory_total']} "
                f"(available: {result.get('memory_available', '?')})\n"
            )

        # Disk
        if "disk_total" in result:
            output.append(
                f"**Disk:** {result.get('disk_used', '?')} / {result['disk_total']} "
                f"(free: {result.get('disk_free', '?')})\n"
            )

        return "\n".join(output)

    # If template not found, return raw JSON
    return f"🔧 **Result from {tool_name}:**\n```json\n{json.dumps(result, ensure_ascii=False, indent=2)}\n```"


def show_help():
    """Show help information"""
    help_text = """
    **Available commands:**

    - `/help` - show this help
    - `/model <name>` - switch model
    - `/exit` or `quit` - exit

    **Available tools:**
    - Find largest file
    - System information
    - Check website
    """
    console.print(Panel(Markdown(help_text), title="Help", border_style="blue"))


def main():
    global model

    history_file = Path.home() / ".ollama_chat_history"
    session = PromptSession(history=FileHistory(str(history_file)))

    # This is ONLY local log (for /history and /save), NOT context for model
    log_messages = []

    console.print(
        Panel.fit(
            "[bold green]Interactive mode with Ollama[/bold green]\n"
            f"Model: [cyan]{model}[/cyan]\n"
            "Type /help for help",
            border_style="green",
        )
    )

    TOOLS = [
        get_json_schema(find_largest_file),
        get_json_schema(get_system_info),
        get_json_schema(check_website),
    ]

    while True:
        try:
            user_input = session.prompt("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Goodbye![/yellow]")
            break

        if not user_input:
            continue

        # Commands
        if user_input.startswith("/"):
            cmd_parts = user_input.split(maxsplit=1)
            cmd = cmd_parts[0]

            if cmd == "/help":
                show_help()
                continue
            elif cmd == "/exit":
                console.print("[yellow]Goodbye![/yellow]")
                break
            elif cmd == "/model" and len(cmd_parts) > 1:
                model = cmd_parts[1]
                console.print(f"[green]Model changed to: {model}[/green]")
                continue
            else:
                console.print(f"[red]Unknown command: {cmd}[/red]")
                continue

        if user_input.lower() in ["quit", "exit"]:
            console.print("[yellow]Goodbye![/yellow]")
            break

        # Log question (locally)
        log_messages.append({"role": "user", "content": user_input})

        DEFAULT_SYSTEM_MSG = (
            "You are a model that can do function calling with the following functions."
        )

        request_messages = [
            {"role": "developer", "content": DEFAULT_SYSTEM_MSG},
            {"role": "user", "content": user_input},
        ]

        try:
            response = chat(
                model,
                messages=request_messages,
                tools=TOOLS,
                options={
                    "top_k": 64,
                    "top_p": 0.95,
                    "temperature": 0.3,
                    "num_ctx": 32768,  # контекст
                },
            )
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            # rollback user message logging
            log_messages.pop()
            continue

        tool_calls = getattr(response.message, "tool_calls", None)

        if tool_calls:
            for tool_call in tool_calls:
                tool_name = tool_call.function.name
                args = tool_call.function.arguments or {}

                console.print(f"[cyan]🔧 Calling: {tool_name}({args})[/cyan]")

                if tool_name == "find_largest_file":
                    result_json = find_largest_file(
                        directory=args.get("directory", ".")
                    )
                elif tool_name == "get_system_info":
                    result_json = get_system_info()
                elif tool_name == "check_website":
                    result_json = check_website(url=args.get("url", ""))
                else:
                    formatted = f"❌ **Model requested unknown tool:** `{tool_name}`"
                    console.print("[bold blue]Assistant:[/bold blue]")
                    console.print(Markdown(formatted))
                    console.print()
                    log_messages.append({"role": "assistant", "content": formatted})
                    continue

                formatted_response = format_tool_response(tool_name, args, result_json)

                console.print("[bold blue]Assistant:[/bold blue]")
                console.print(Markdown(formatted_response))
                console.print()

                # log response (locally), but DON'T use as context
                log_messages.append(
                    {"role": "assistant", "content": formatted_response}
                )

        else:
            formatted = (
                "❌ **No tool found for request.**\n\n"
                "Available tools:\n"
                "- 📁 `find_largest_file` — example: `folder /home`\n"
                "- 🌐 `check_website` — example: `site ya.ru`\n"
                "- 🖥️ `get_system_info` — example: `system information`\n"
            )
            console.print("[bold blue]Assistant:[/bold blue]")
            console.print(Markdown(formatted))
            console.print()

            log_messages.append({"role": "assistant", "content": formatted})


if __name__ == "__main__":
    main()
