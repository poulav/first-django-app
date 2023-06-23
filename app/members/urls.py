from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('allmembers/', views.allmembers, name='allmembers'),
    path('allmembers/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('test/', views.test, name='test'),
]
