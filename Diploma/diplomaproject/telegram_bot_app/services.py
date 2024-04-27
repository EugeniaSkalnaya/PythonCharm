import httpx
from diplomaproject import settings


async def post_event_on_telegram(message):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=payload)
        return response.json()