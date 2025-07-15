from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import MovieViewSet, MovieSessionViewSet


app_name = "cinema"

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"moviesessions", MovieSessionViewSet)  # <- важливо

urlpatterns = [
    path("", include(router.urls)),
]
