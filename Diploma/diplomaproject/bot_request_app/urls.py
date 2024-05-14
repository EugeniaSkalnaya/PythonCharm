from django.urls import path
from bot_request_app.views import send_telegram_message



urlpatterns = [
    path('send_message/', send_telegram_message, name='send_message'),
]