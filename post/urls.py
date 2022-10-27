from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('post/', views.PostListCreateView.as_view()),
    path('post/<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view()),
]

