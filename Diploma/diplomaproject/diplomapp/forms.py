from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Diploma


User = get_user_model()


class SpecialistRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SpecialistProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'patronimic', 'phonenumber', 'about',
                  "age", "gender", "avatar", "city"]


class DiplomaForm(forms.ModelForm):
    class Meta:
        model = Diploma
        fields = ["diploma_name", "diploma_upload"]