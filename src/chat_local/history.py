import json
from pathlib import Path

def load_history(path):
    if not path.exists():
        return []

    try:
        return json.loads(path.read_text(encoding="utf-8"))
        
    except json.JSONDecodeError:
        print("Warning: history file is invalid")
        return []

def save_history(path, messages):
    path.write_text(
        json.dumps(messages, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
