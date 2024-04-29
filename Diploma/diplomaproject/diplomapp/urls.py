from django.urls import path, include
from . import views



urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('profile_logged/', views.show_logged_profile, name="show_logged_profile"),
    path('profile/<int:pk>/', views.show_profile, name="show_profile"),
    path('profile/update', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/update/success/', views.ProfileUpdateSuccessView.as_view(), name='profile_success'),
    path('diplomas/', views.show_diplomas, name='show_diplomas'),
    path('profile/upload_diploma/', views.upload_diploma, name='upload_diploma'),
    path('profile/diplomas', views.show_diplomas, name='show_diplomas'),
    path("catalogue", views.catalogue, name="catalogue"),
    ]