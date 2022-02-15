from django.urls import path
from app.views import search, detail

urlpatterns = [
    path('search/', search, name='search'),
    path('<str:platform>/<str:name>/', detail, name='detail')
]
