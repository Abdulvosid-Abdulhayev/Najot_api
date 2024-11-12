from django.urls import path
from .views import IndexView
urlpatterns = [
    path("api/v1/", IndexView.as_view())
]

