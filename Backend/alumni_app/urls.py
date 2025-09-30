from django.urls import path
from .views import RegisterView, CategoryListView, SubcategoryListView, ProfilesBySubcategoryView, ProfileDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("categories/", CategoryListView.as_view()),
    path("categories/<int:category_id>/subcategories/", SubcategoryListView.as_view()),
    path("subcategories/<int:sub_id>/profiles/", ProfilesBySubcategoryView.as_view()),
    path("profile/<str:username>/", ProfileDetailView.as_view()),
]
