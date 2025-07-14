from django.urls import path
from . import views

app_name = "cinema"

urlpatterns = [
    path("", views.MovieListView.as_view(), name="movie-list"),
    path("<int:pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
    # додайте інші шляхи за потребою
]