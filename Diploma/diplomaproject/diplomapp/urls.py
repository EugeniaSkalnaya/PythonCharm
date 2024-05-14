from django.urls import path, include
from . import views



urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('profile_logged/', views.show_logged_profile, name="show_logged_profile"),
    path('profile/<int:pk>/', views.show_profile, name="show_profile"),
    path('profile/update', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/update/success/', views.ProfileUpdateSuccessView.as_view(), name='profile_success'),
    path("catalogue", views.catalogue, name="catalogue"),
    path("error", views.predictable_error, name="predictable_error"),
    path("form_sucess", views.form_success, name="form_success"),
    ]