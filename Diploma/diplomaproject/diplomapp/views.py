from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView

from .forms import SpecialistRegistrationForm, SpecialistProfileForm
from .models import Profile


def index(request):
    print(request.user)
    return render(request, 'index.html')


def form_success(request):
    return render(request, 'form_success.html')


def register(request):
    """Представление для регистрации нового исполнителя"""
    if request.method == 'POST':
        form = SpecialistRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return render(request, "index.html")
        return predictable_error(request)
    else:
        form = SpecialistRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """представление для обновления информации в профиле пользователя"""
    model = Profile
    form_class = SpecialistProfileForm
    template_name = "specialist_profile_update.html"
    success_url = reverse_lazy('profile_success')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('profile_success')


class ProfileUpdateSuccessView(TemplateView):
    template_name = 'profile_success.html'


def predictable_error(request):
    return render(request, "error.html")


def login_view(request):
    """Представление для аутентификации исполнителя"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('index')
        else:
            return predictable_error(request)
    return render(request, 'login.html')


def show_logged_profile(request):
    """ Показывает профиль конкретного пользователя"""
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def show_profile(request, pk):
    """ Показывает профиль конкретного пользователя"""
    profile = Profile.objects.get(pk=pk)
    return render(request, 'profile.html', {'profile': profile})


def catalogue(request):
    """Отображение всех исполнителей сайта в каталоге"""
    specialists = Profile.objects.exclude(user="1")
    return render(request, 'catalogue.html', {'specialists': specialists})
