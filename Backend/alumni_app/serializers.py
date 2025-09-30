from rest_framework import serializers
from .models import User, Profile, ProfessionCategory, ProfessionSubcategory
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", "")
        )
        user.set_password(validated_data["password"])
        user.save()
        Profile.objects.create(user=user)  # create profile automatically
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ["user", "batch_year", "bio", "subcategory", "linkedin", "github", "portfolio", "contact_email"]

class ProfessionSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionSubcategory
        fields = ["id", "name", "slug", "category"]

class ProfessionCategorySerializer(serializers.ModelSerializer):
    subcategories = ProfessionSubcategorySerializer(many=True, read_only=True)
    class Meta:
        model = ProfessionCategory
        fields = ["id", "name", "slug", "subcategories"]
