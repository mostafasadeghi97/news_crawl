from django.contrib import admin
from django.urls import path, include
from .views import search_term, term_autocomplete


urlpatterns = [
    path('', search_term),
    path('auto/', term_autocomplete),
]
