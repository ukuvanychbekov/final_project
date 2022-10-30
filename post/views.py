from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, TokenAuthentication


import telebot

from account.models import User
from .models import Post, Comment, Mark
from .serializer import PostSerializer, CommentSerializer, MarkSerializer
from .permissions import BasePermission, CommentPermission, MarkPermission

bot = telebot.TeleBot('5608904760:AAE0WksRvOLl21_Co-RZl6yFxnzLOMTXpOc', parse_mode=None)


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission, ]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            for i in User.objects.filter(username=self.request.user):
                bot.send_message(i.telegram, 'Блог создан')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission ]


class CommentListCreateAPIView(ListCreateAPIView):
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
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [CommentPermission, ]


class MarkListCreateView(ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [MarkPermission]


class MarkRetrieveDestroyUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [MarkPermission]








