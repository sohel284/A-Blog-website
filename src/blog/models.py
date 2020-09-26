from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author', )
    blog_title = models.CharField(max_length=264, )
    slug = models.SlugField(max_length=264, unique=True, )
    blog_content = models.TextField(verbose_name='What is on your mind?', )
    blog_image = models.ImageField(upload_to='blog-image', verbose_name='Image')
    publish_date = models.DateTimeField(auto_now_add=True, )
    update_date = models.DateTimeField(auto_now=True, )

   
   

    class Meta:
        db_table = 'blog'
        ordering = ('-publish_date', )


    
        

    def __str__(self):
        return self.blog_title    


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment', )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment', )
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, )

    class Meta:
        db_table = 'comment'
        ordering = ('-comment_date', )
       
       
       
    
    def __str__(self):
        return self.comment


class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')      

    class Meta:
        db_table = 'likes'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'  

    def __str__(self):
        return self.user + 'likes' + self.blog    


     
