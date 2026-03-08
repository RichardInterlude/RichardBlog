from .models import Post, Category, Tag, Comment
from rest_framework import serializers


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CtaegorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommenntSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
