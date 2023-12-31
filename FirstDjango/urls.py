from django.contrib import admin
from django.urls import path

from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/<int:id_item>', views.get_items, name='items'),
    path('items/', views.list_items, name='items-list'),
]
