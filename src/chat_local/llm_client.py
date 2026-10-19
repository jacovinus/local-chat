import httpx


def ask_model(config, messages):
    response = httpx.post(
        config["api_url"],
        json={
            "model":config["model_name"],
            "messages": messages,
            "max_tokens": config["max_tokens"],
            "stream": False,
        },
        timeout=config["timeout"],
    )

    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"]
