from django.urls import path
from telegram_bot_app.views import send_telegram_message



urlpatterns = [
    path('send_message/', send_telegram_message, name='send_message'),
]