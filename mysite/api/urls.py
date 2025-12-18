from os import name

from django.urls import path

from . import views

urlpatterns = [
path('blogposts/',views.BlogPostListCreate.as_view(),name='blogpost-view-create'),
path('blogposts/<int:pk>/',views.BlogRetrieveUpdateDestroy.as_view(), name="update"),
path('blog/',views.BlogPostList.as_view(), name="blog"),
]