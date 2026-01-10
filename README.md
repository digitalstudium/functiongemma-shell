# FunctionGemma Shell

A conversational AI assistant powered by Ollama with function calling capabilities for system operations.

## Features

- 🤖 Interactive chat interface with function calling support
- 🔧 Built-in tools for system operations:
  - **File Search**: Find the largest file in a directory
  - **System Info**: Get OS, CPU, memory, and disk information
  - **Website Check**: Check website availability and response time
- 💬 Command history with persistent storage
- 🎨 Rich terminal UI with syntax highlighting
- 🔄 Model switching on the fly

## Requirements

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- FunctionGemma model (or any other model with function calling support)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/digitalstudium/functiongemma-shell
cd functiongemma-shell
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Pull the FunctionGemma model (if not already installed) and run ollama:
```bash
ollama pull functiongemma
ollama serve
```

## Usage

Run the chat interface:
```bash
python chat.py
```

### Available Commands

- `/help` - Show help information
- `/model <name>` - Switch to a different model
- `/exit` - Exit the application

You can also type `выход`, `quit`, or `exit` to quit.

### Example Interactions

**Check system information:**
```
You: system information
```

**Find largest file:**
```
You: find the largest file in /home
```

**Check website:**
```
You: check if google.com is available
```

## Available Tools

### 1. `find_largest_file`
Finds the largest file in a specified directory using bash commands.

**Arguments:**
- `directory` (optional): Path to search (default: current directory)

### 2. `get_system_info`
Retrieves basic system information including OS, hostname, CPU cores, memory, and disk usage.

**No arguments required**

### 3. `check_website`
Checks website availability and measures response time.

**Arguments:**
- `url`: Website URL (protocol optional, e.g., "google.com" or "https://github.com")

## Project Structure

```
functiongemma-shell/
├── chat.py              # Main application file
├── requirements.txt     # Python dependencies
└── venv/               # Virtual environment (generated)
```

## Dependencies

- `ollama` - Ollama Python client
- `prompt-toolkit` - Interactive command-line interface
- `rich` - Terminal formatting and markdown rendering

## Configuration

The default model is set to `functiongemma`. You can change it by:
1. Editing the `model` variable in `chat.py`
2. Using the `/model <name>` command during runtime

## Chat History

Command history is automatically saved to `~/.ollama_chat_history` for persistence across sessions.

## Notes

- The application runs each query independently (stateless) - previous context is not preserved between queries
- Tool execution timeout is set to 30 seconds for file operations
- Website checks have a 5-second timeout
- All tool responses are formatted with rich markdown output

## License

[Your License Here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
