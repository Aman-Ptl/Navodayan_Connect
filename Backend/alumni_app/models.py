from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_alumni = models.BooleanField(default=True)

class ProfessionCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class ProfessionSubcategory(models.Model):
    category = models.ForeignKey(ProfessionCategory, related_name="subcategories", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    batch_year = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)
    subcategory = models.ForeignKey(ProfessionSubcategory, null=True, blank=True, on_delete=models.SET_NULL, related_name="profiles")
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)

    def __str__(self):
        return self.user.username
