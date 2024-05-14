from django.urls import path
from bot_support_app.views import send_tg_support_message

urlpatterns = [
    path('send_support/', send_tg_support_message, name='send_tg_support_message'),
]