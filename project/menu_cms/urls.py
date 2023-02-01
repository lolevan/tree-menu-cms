from django.urls import path

from . import views


urlpatterns = [
    path('', views.link_view, name='main_menu'),
    path('menu/<path:item>/', views.menu_view),
]
