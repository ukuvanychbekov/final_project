from django.urls import path

from . import views


urlpatterns = [
    path('post/', views.PostListCreateView.as_view()),
    path('post/<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view()),
    path('post/<int:post_id>/comment/', views.CommentListCreateAPIView.as_view()),
    path('post/<int:post_id>/comment/<int:pk>/', views.CommentRetrieveDestroyUpdateAPIView.as_view()),
    path('post/mark', views.MarkListCreateView.as_view()),
    path('post/mark/<int:pk>/', views.MarkRetrieveDestroyUpdateAPIView.as_view()),
    ]