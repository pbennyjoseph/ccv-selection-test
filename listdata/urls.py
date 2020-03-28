from django.urls import path

from .views import *

urlpatterns = [
    path('search/', searchview, name='search'),
    path('', orderedlistview, name='home'),
]