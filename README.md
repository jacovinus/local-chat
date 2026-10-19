# chat-local

A small Python command-line client for chatting with a local language model running with llama.cpp.

## Requirements

- macOS, Linux, or Windows
- Python
- uv
- llama.cpp

## Install llama.cpp

On macOS with Homebrew:

```bash
brew install llama.cpp
```

## Download and start a model

llama.cpp can download a GGUF model from Hugging Face and start the local server in one command:

```bash
llama-server \
  -hf SC117/LFM2.5-2.6B-Uncensored-GGUF:Q4_K_M \
  --alias local-model \
  --jinja \
  -ngl 99 \
  -c 8192 \
  --port 8081
```

The model is downloaded locally the first time it is started. Later executions reuse the cached files.

The local server runs at:

```text
http://127.0.0.1:8081
```

## Using an existing GGUF file

If the model has already been downloaded manually:

```bash
llama-server \
  -m /path/to/model.gguf \
  --alias local-model \
  --jinja \
  -ngl 99 \
  -c 8192 \
  --port 8081
```

Replace `/path/to/model.gguf` with the path to the local file.

## Project setup

Install the Python dependencies:

```bash
uv sync
```

Configure `config.yaml`:

```yaml
api_url: "http://127.0.0.1:8081/v1/chat/completions"
model_name: "local-model"
history_file: "chat_history.json"
max_tokens: 512
timeout: 120.0
```

Start the chat:

```bash
uv run chat-local
```

## Commands

Inside the chat:

```text
exit
```

Exit the application.

```text
clear
```

Clear the local conversation history.

Conversation history is stored in:

```text
chat_history.json
```

## Project structure
├── config.yaml
├── main.py
├── pyproject.toml
├── uv.lock
└── src/
    └── chat_local/
        ├── __init__.py
        ├── chat.py
        ├── config.py
        ├── history.py
        └── llm_client.py
