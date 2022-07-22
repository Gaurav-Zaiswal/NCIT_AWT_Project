from . import views
from django.urls import path

app_name = 'socialapp'
urlpatterns= [
    path('home/', views.home, name='home'),
    # path('profile/<str:name>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]