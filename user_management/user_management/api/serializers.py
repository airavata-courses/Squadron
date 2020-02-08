from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True, 'allow_blank': False}}

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save(owner=self.request.user)
        print(user)
        return user

    # Users are not allowed to update their passwords and a separate screen is provided for that
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        return instance
