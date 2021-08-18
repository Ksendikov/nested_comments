from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    content = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['content']

    def __str__(self):
        return self.content


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey(
        'self',
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children')
    comment = models.TextField()
    comment_created_date = models.DateTimeField(default=timezone.now)

    class MPTTMeta:
        order_insertion_by = ['post']

    def __str__(self):
        return self.comment
