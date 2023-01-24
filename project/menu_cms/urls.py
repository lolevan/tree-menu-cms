from django.urls import path

from . import views


urlpatterns = [
    path('', views.test_menu_view, name='menu'),
]
