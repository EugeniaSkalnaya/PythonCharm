from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import CustomerForm
from .services import post_event_on_telegram


async def send_telegram_message(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            message = f"Имя: {form.cleaned_data['name']}\n" \
                      f"Контакты: {form.cleaned_data['phone_number']}\n" \
                      f"Пол исполнителя: {form.cleaned_data['gender']}\n" \
                      f"Заявка: {form.cleaned_data['text']}"
            await post_event_on_telegram(message)
            return render(request, 'index.html', {'form': form})
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})



