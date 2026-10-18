from django.urls import path

from penguins.penguins.urls import urlpatterns
from .views import hello_view

urlpatterns = [
        path('', hello_view, name = "home")
]