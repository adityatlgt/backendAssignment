from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

# To serilize the user data.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'email', 'password')

    # to encrypt the user password.
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

# To add the data post in modal
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'pub_date') # Added required fields only.


