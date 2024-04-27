from django import forms


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=50,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Как можно к вам обращаться'}))
    phone_number = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=[('M', 'Мужчина'), ('F', 'Женщина')],
                                   widget=forms.Select(attrs={'class': 'form-check-input'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                            'placeholder': 'Опишите вашу проблему, чтобы с вами мог связаться подходящий специалист'}))
