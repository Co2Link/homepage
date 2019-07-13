from django.db import models


class Comment(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(max_length=255)

    url = models.URLField(blank=True)

    body = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]
