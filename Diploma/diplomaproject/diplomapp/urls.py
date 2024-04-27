from django.urls import path, include
from . import views



urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('specialist_profile_update/', views.specialist_profile_update, name='specialist_profile_update'),
    path('profile/', views.show_profile, name="show_profile"),
    path('diplomas/', views.show_diplomas, name='show_diplomas'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/upload_diploma/', views.upload_diploma, name='upload_diploma'),
    path('profile/diplomas', views.show_diplomas, name='show_diplomas'),
    path("catalogue", views.catalogue, name="catalogue"),
    path('upprofile/', views.upprofile, name='upprofile'),
]