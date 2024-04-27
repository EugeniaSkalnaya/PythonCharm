from django.shortcuts import render
from .forms import TechSupportForm
from .services import post_event_on_telegram



async def send_tg_support_message(request):
    if request.method == 'POST':
        form = TechSupportForm(request.POST)
        if form.is_valid():
            message = f"Name: {form.cleaned_data['name']}\n" \
                      f"Contact: {form.cleaned_data['phone_number']}\n" \
                      f"Text: {form.cleaned_data['text']}"
            await post_event_on_telegram(message)
            return render(request, 'index.html', {'form': form})
    else:
        form = TechSupportForm()
    return render(request, 'tech_support.html', {'form': form})



