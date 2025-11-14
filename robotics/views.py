from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost,Tutorial
from .serializers import BlogPostSerializer,TutorialSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
# Create your views here.

# Tutorials API
class TutorialListCreateView(generics.ListCreateAPIView):
    serializer_class = TutorialSerializer

    def get_queryset(self):
        queryset = Tutorial.objects.all().order_by("-created_at")
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category.lower())
        return queryset


class TutorialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
