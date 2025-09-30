from django.urls import path, include

urlpatterns = [
    path("api/", include("alumni_app.urls")),
]
