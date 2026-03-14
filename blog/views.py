from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . serializers import PostSerializers, CategorySerializers, TagSerializers, CommentSerializers
from . models import Post, Category, Tag, Comment

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


# :::: CATEGORY VIEW ::::
class CategoryView(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            serializer  = CategorySerializers(data=request.data, user = request.user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,{'message':'Post Created Successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request):
        try:
            category = Category.objects.get(user= request.user)
            serializers = CategorySerializers(category, many = True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategorysView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request, slug):
        try:
            category = get_object_or_404(Category, slug=slug, user = request.user)
            serializers = CategorySerializers(category, many = True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, slug):
        try:
            category = get_object_or_404(Category, slug=slug)
            serializers = CategorySerializers(category, data=request.data, partial =True)
            if serializers.is_valid():
                serializers.save()
                return Response({'Message':'Blog Post updated Successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# :::: BlogPost VIEW ::::
class PostView(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            serializer  = PostSerializers(data=request.data, user = request.user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,{'message':'Post Created Successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request):
        try:
            blog = Post.objects.get(user= request.user)
            serializers = PostSerializers(blog, many = True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)     

class PostsView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def get(self, request, slug):
        try:
            blog = get_object_or_404(Post, slug=slug, user = request.user)
            serializers = PostSerializers(blog, many = True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, slug):
        try:
            blog = get_object_or_404(Post, slug=slug)
            serializers = PostSerializers(blog, data=request.data, partial =True)
            if serializers.is_valid():
                serializers.save()
                return Response({'Message':'Blog Post updated Successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TagView(APIView):
    def get(self, request, slug):
        try:
            tag = Tag.objects.filter(slug=slug)
            serializers = TagSerializers(tag, many = True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# :::: COMMENT VIEW ::::      
class CommentView(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request, user):
        try:
            serializers = CommentSerializers(data = request.data, user = request.user)
            if serializers.is_valid():
                serializers.save()
                return Response({'Message':'Your Comment was successfully added'})
        except Exception as e:
            return Response ({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)