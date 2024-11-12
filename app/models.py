from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True) 
    
    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "name": self.name,
            "slug": self.slug,
            "image": self.image.url if self.image else None,  
        }

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default=None)
    about = models.CharField(max_length=255)
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)  
    def __str__(self):
        return self.title
    
    def to_dict(self):
        return {
            "title": self.title,
            "slug": self.slug,
            "about": self.about,
            "published_date": self.published_date,
            "category": self.category_id,
            "author": self.author,
            "image": self.image.url if self.image else None,  
        }

class Comment(models.Model):
    title = models.CharField(max_length=63)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    comment_text = models.TextField()
    comment_date = models.DateField()
    image = models.ImageField(upload_to='comment_images/', blank=True, null=True)  
    
    def __str__(self):
        return self.title
    
    def to_dict(self):
        return {
            "title": self.title,
            "article": self.article_id,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "comment_text": self.comment_text,
            "comment_date": self.comment_date,
            "image": self.image.url if self.image else None,  
        }
