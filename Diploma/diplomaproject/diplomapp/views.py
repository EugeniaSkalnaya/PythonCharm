import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View

from .forms import SpecialistRegistrationForm, DiplomaForm,SpecialistProfileForm#, UserCreationForm
from .models import SpecialistProfile, Diploma

logger = logging.getLogger(__name__)


def index(request):
    print(request.user)
    return render(request, 'index.html')


def register(request):
    """Представление для регистрации нового исполнителя"""
    if request.method == 'POST':
        form = SpecialistRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "index.html")
    else:
        form = SpecialistRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



#не работает
@login_required
def specialist_profile_update(request):
    """Представление для обновления информации профиля для аутентифицированного пользователя"""
    profile = get_object_or_404(SpecialistProfile, user=request.user)
    if request.method == 'POST':
        form = SpecialistProfileForm(request.POST, instance=profile)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            patronimic = form.cleaned_data['patronimic']
            #email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            about = form.cleaned_data['about']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            avatar = form.cleaned_data['avatar']
            fs = FileSystemStorage()
            fs.save(avatar.name, avatar)
            logger.info(f'Получили все необходимые данные от специалиста.')
            specialist_profile = SpecialistProfile(
                firstname=firstname,
                lastname=lastname,
                patronimic=patronimic,
                # email=email,
                phonenumber=phonenumber,
                about=about,
                age=age,
                gender=gender,
                avatar=avatar
            )
            specialist_profile.save()
            form.save()
            return redirect('catalogue')
            #return redirect(request, 'catalogue', {'form': specialist_profile})
    else:
        form = SpecialistProfileForm(instance=request.user.profileprofile)
    return render(request, 'specialist_profile_update.html', {'form': form})



#пока не работает
@login_required
@transaction.atomic()
def update_profile(request):
    if request.method == 'POST':
        u_form = SpecialistRegistrationForm(request.POST, instance=request.user)
        p_form = SpecialistProfile(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('index') # Redirect back to profile page
        else:
            messages.error(request, "please correct your data")
    else:
        u_form = SpecialistRegistrationForm(instance=request.user)
        p_form = SpecialistProfile(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'diplomapp/profile.html', context)


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
            return HttpResponse('Аккаунт не найден')
    return render(request, 'login.html')


def upprofile(request):
    if request.method == 'POST':
        form = SpecialistProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SpecialistProfileForm(instance=request.user)
    return render(request, 'specialist_profile_update.html', {'form': form})


def show_profile(request):
    """ Показывает профиль конкретного пользователя"""
    profile = SpecialistProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def catalogue(request):
    """Отображение всех исполнителей сайта в каталоге"""
    specialists = SpecialistProfile.objects.all()
    return render(request, 'catalogue.html', {'specialists': specialists})

#пока не реализовано и возможно стоит убрать
def show_diplomas(request):
    diplomas = Diploma.objects.all()
    return render(request, 'diplomas.html', {'diplomas': diplomas})


@login_required
def upload_diploma(request):
    """Загрузка дипломов в профиль исполнителя, работает только для залогиненных пользователей"""
    if request.method == 'POST':
        form = DiplomaForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['diploma_upload']
            text = form.cleaned_data['diploma_name']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            diploma = Diploma(
                diploma_upload=image,
                diploma_name=text
            )
            diploma.save()
    else:
        form = DiplomaForm()
    return render(request, 'profile.html', {'form': form})
