from rest_framework import generics, permissions
from .models import ProfessionCategory, ProfessionSubcategory, Profile
from .serializers import ProfessionCategorySerializer, ProfessionSubcategorySerializer, ProfileSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CategoryListView(generics.ListAPIView):
    queryset = ProfessionCategory.objects.all()
    serializer_class = ProfessionCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SubcategoryListView(generics.ListAPIView):
    serializer_class = ProfessionSubcategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ProfessionSubcategory.objects.filter(category_id=self.kwargs["category_id"])

class ProfilesBySubcategoryView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Profile.objects.filter(subcategory_id=self.kwargs["sub_id"]).select_related("user")

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "user__username"
    queryset = Profile.objects.all()
