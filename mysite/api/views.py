from django.shortcuts import render
from rest_framework import generics, status, request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost
from .serializers import BlogPostSerializers
# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    def delete(self,request,*args,**kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self,request):
        title = request.query_params.get("title")
        if title:
            blog_posts = BlogPost.objects.all().filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializers(title,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)