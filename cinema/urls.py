from django.urls import path
from . import views

app_name = "cinema"

urlpatterns = [
    path("<int:pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
]
