from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Comment, Article, Category


class IndexView(APIView):
    def get(self, request: Request) -> Response:
        coments = Comment.objects.all()
        articles = Article.objects.all()
        categories = Category.objects.all()
        
        data = {
            "comments": [comment.to_dict() for comment in coments],
            "articles": [article.to_dict() for article in articles],
            "categories": [category.to_dict() for category in categories]
               }
        
        return Response({"message": "Welcome to the API!", "data": data})