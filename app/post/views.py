from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.conf import settings

import telebot
import os

from account.models import User
from .models import Post, Comment, Mark
from .serializer import PostSerializer, CommentSerializer, MarkSerializer
from .permissions import BasePermission, CommentPermission, MarkPermission

bot = telebot.TeleBot(os.environ.get('TOKEN'), parse_mode=None)


class PostListCreateView(ListCreateAPIView):
    """
    Blog API endpoint to get list of blogs and create blogs
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission, ]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            try:
                for i in User.objects.filter(username=self.request.user):
                    bot.send_message(i.telegram, 'Пост успешно создан!')
            except:
                pass

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Blog API endpoint to retrieve, update and delete blogs
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission ]


class CommentListCreateAPIView(ListCreateAPIView):
    """
    Blog API endpoint to get list of blogs and create blogs
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        try:
            serializer.save(
                user=self.request.user,
                post=get_object_or_404(Post, id=self.kwargs['post_id'])
            )
        except ValueError:
            serializer.save(
                post=get_object_or_404(Post, id=self.kwargs['post_id'])
            )


class CommentRetrieveDestroyUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """
    Blog API endpoint to retrieve, update and delete blogs
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [CommentPermission, ]


class MarkListCreateView(ListCreateAPIView):
    """
    Blog API endpoint to get list of blogs and create blogs
    """
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [MarkPermission]

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])
    def perform_create(self, serializer):
        try:
            serializer.save(
                auth=self.request.user,
                post=get_object_or_404(Post, id=self.kwargs['post_id'])
            )
        except ValueError:
            serializer.save(
                post=get_object_or_404(Post, id=self.kwargs['post_id'])
            )



class MarkRetrieveDestroyUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """
    Blog API endpoint to retrieve, update and delete blogs
    """
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [MarkPermission]








