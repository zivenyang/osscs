from django.urls import path
from app.views import PackageList, PackageDetail

urlpatterns = [
    path('search/', PackageList.as_view(), name='search'),
    path('<str:platform>/<str:name>/', PackageDetail.as_view(), name='detail')
]
