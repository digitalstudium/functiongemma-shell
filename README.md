# FunctionGemma Shell (Experimental)

A small **experimental terminal chat tool** built to demonstrate how **FunctionGemma** (via **Ollama tool/function calling**) can be used from the command line to run simple “tools” (system/utility functions) and render results nicely in the terminal.

This project is **for demo / exploration purposes only**—it is not production-ready and it intentionally keeps the conversation **stateless** (each request is sent without previous context).

## What this is (and what it isn’t)

- This **is** a minimal CLI wrapper around `ollama.chat(...)` that exposes a few Python functions as tools.
- This **is** meant to help you quickly test how a tool-calling model behaves in a terminal workflow.
- This **is not** a secure shell, remote admin tool, or a production chatbot.
- This **does not** maintain chat context across turns (by design).

## Features

- Interactive terminal UI (prompt, history, markdown rendering)
- Ollama chat integration with **tools/function calling**
- Built-in demo tools:
  - `find_largest_file(directory)` — find the largest file under a directory (uses `find/du/sort`)
  - `get_system_info()` — basic OS/CPU/memory/disk info
  - `check_website(url)` — HTTP status + latency check

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- A tool-calling capable model (default: `functiongemma`)

## Setup

```bash
git clone <your-repo-url>
cd functiongemma-shell

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Pull the model:

```bash
ollama pull functiongemma
```

## Run

```bash
python chat.py
```

You should see an interactive prompt:

- `You:` — your input
- `Assistant:` — formatted tool output (Markdown rendered via `rich`)

## Commands

- `/help` — show help
- `/model <name>` — switch Ollama model at runtime
- `/exit` — quit

## Example prompts to trigger tools

Try natural language—FunctionGemma decides whether to call a tool.

- Largest file:
  - “Find the largest file in /home”
  - “Largest file in ./”
- System info:
  - “Show system info”
  - “CPU cores and memory”
- Website check:
  - “Check google.com”
  - “Is https://github.com reachable?”

## Notes / Limitations (Important)

- **Stateless by design:** the script does not feed previous messages back to the model.
- **Local-only demo:** tools run on your machine with your permissions.
- **Shell command usage:** `find_largest_file` uses shell commands (`find`, `du`, `sort`). This is a demo and not hardened against malicious input.
- **Tool coverage is minimal:** only three tools are included to demonstrate the concept.

## Project structure

```
.
├── chat.py
└── requirements.txt
```

## Disclaimer

This is an **experimental demo tool** showing how FunctionGemma-style tool calling can be used from a terminal. Use at your own risk. Do not run it on machines where executing local commands could be unsafe.
