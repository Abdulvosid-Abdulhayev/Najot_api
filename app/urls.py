from django.urls import path
from .views import CategoryView, ArticleView, AuthorView

urlpatterns = [
    path('api/v1/categories/', CategoryView.as_view()),           
    path('api/v1/categories/<int:pk>/', CategoryView.as_view()), 
    path('api/v1/articles/', ArticleView.as_view()),              
    path('api/v1/articles/<int:pk>/', ArticleView.as_view()),     
    path('api/v1/authors/', AuthorView.as_view()),                
]