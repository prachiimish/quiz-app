from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),  # Show the quiz when the user visits the root URL
]
