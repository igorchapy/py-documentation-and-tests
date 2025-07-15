from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import MovieViewSet


app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")  # basename дуже важливий

urlpatterns = [
    path("", include(router.urls)),
]
