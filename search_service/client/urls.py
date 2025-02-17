from django.urls import path
from .views import search_view

urlpatterns = [
    path('search/api/', search_view, name='search')
]