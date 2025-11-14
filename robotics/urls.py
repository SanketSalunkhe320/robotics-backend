from django.urls import path
from .views import BlogPostListCreate, BlogPostDetail, TutorialListCreateView, TutorialDetailView

urlpatterns = [
    path('blog/', BlogPostListCreate.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogPostDetail.as_view(), name='blog-detail'),

    # Tutorials
    path("tutorials/", TutorialListCreateView.as_view(), name="tutorial-list"),
    path("tutorials/<int:pk>/", TutorialDetailView.as_view(), name="tutorial-detail"),
]
