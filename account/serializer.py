from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from .models import UserProfile


class RegisterSerilalizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password, ])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'telegram', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError('Password do not match')
        return data

    def create(self, validated_data):
        user = UserProfile(
            username=validated_data['username'],
            email=validated_data['email'],
            telegram=validated_data['telegram']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user