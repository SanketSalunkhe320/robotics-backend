from rest_framework import serializers
from .models import BlogPost,Tutorial

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = "__all__"
