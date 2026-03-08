from rest_framework import serializers
from . models import Profile, User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'profile_pix', 'phone_number', 'role', 'social_media']

class RegisterationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'password1', 'name', 'bio', 'profile_pix', 'phone_number', 'role', 'social_media']

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError("Passwords do not match. Dont be dumb")
        return data
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        

        user = User.objects.create_user(username=username, email=email, password=password)

        profile = Profile.objects.create(
            user=user,
            name=validated_data['name'],
            bio=validated_data['bio'],
            profile_pix=validated_data['profile_pix'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            social_media=validated_data['social_media']
        )
        return profile