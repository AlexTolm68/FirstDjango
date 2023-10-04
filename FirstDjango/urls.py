from django.contrib import admin
from django.urls import path

from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('items/<int:id_item>', views.get_items),
    path('items/', views.list_items),
]
