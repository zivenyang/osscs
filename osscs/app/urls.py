from django.urls import path, include
from app.views import search

urlpatterns = [
    path('search/', search, name='search')
]
