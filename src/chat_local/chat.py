from pathlib import Path

import httpx

from .config import load_config
from .history import load_history, save_history
from .llm_client import ask_model

SYSTEM_PROMPT = (
    "You are helpful local coding assistant. "
    "Give concise, accurate explanations and practical examples."
)

def run_chat():
    config = load_config()
    history_path = Path(config["history_file"])
    messages = load_history(history_path)

    if not messages:
        messages.append({
                            "role": "system",
                            "content": SYSTEM_PROMPT,
                        })
        print("Local chat - type 'exit' to quit or 'clear' to clear history.")

        while True:
            user_input = input("\nYou: ").strip()

            if user_input.lower() == "exit":
                save_history(history_path, messages)
                print("Goodbye!")
                return

            if user_input.lower() == "clear":
                messages = [{
                    "role":"system",
                    "content": SYSTEM_PROMPT,
                }]
                save_history(history_path, messages)
                print("History cleared.")
                continue

            if not user_input:
                continue

            user_message = {
                "role": "user",
                "content": user_input,
            }

            print("\nThinking...")

            try:
                reply = ask_model(config, messages + [user_message])
            except httpx.HTTPError as error:
                print(f"\nRequest failed: {error}")
                continue

            messages.extend([
                                user_message,
                                {
                                    "role":"assistant",
                                    "content": reply
                                },
                            ])

            save_history(history_path, messages)
            print(f"\Assistant: {reply}")
