from django.contrib import admin
from django.urls import path

from .views import HomePageView, FetchDataView

urlpatterns = [
    path('', HomePageView.as_view(), name = "index"),
    path('data', FetchDataView.as_view(), name = "data"),
]
