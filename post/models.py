from django.db import models
from django.db.models import Avg

from account.models import User

from django.db.models import Avg


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def average_rating(self):
        average = Mark.objects.filter(post=self).aggregate(Avg('mark_number'))
        for i in average.values():
            return i

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    author_name = models.CharField(max_length=50, blank=True, null=True, help_text="Только для авторизованных")
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text


class Mark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    mark_number = models.IntegerField(choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ], null=True, blank=True)

    class Meta:
        unique_together = ('post', 'auth')

    def __str__(self):
        return self.post.text




