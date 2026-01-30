import os
import requests

def send(text, timeout=30):
    token = os.getenv("VAWATCH_TELEGRAM_TOKEN")
    chat_id = os.getenv("VAWATCH_TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        raise RuntimeError("VAWATCH_TELEGRAM_TOKEN or VAWATCH_TELEGRAM_CHAT_ID not set")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    r = requests.post(
        url,
        data={"chat_id": chat_id, "text": text[:4096]},
        timeout=timeout,
    )
    r.raise_for_status()
