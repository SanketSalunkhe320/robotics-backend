from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Tutorial(models.Model):
    CATEGORY_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    DIFFICULTY_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    title = models.CharField(max_length=255)
    link = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    duration = models.CharField(max_length=50)  # e.g., "30 min"
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    tags = models.JSONField(default=list)   # ["Installation", "Setup", "Environment"]

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


