from rest_framework import serializers

from .models import Post, Comment, Mark


class PostSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'post']


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = '__all__'
        read_only_fields = ['post', 'auth'  ]

