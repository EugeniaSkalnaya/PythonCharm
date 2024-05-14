from django import forms


class TechSupportForm(forms.Form):
    name = forms.CharField(max_length=50,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Как можно к вам обращаться'}))
    phone_number = forms.CharField(max_length=15)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                            'placeholder': 'Опишите вашу проблему'}))
