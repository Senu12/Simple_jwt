from django.db import models

# Create your models here.


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=40)
    picture = models.ImageField(upload_to='my_picture', blank=True)
    created_by = models.ForeignKey(
        'auth.user', related_name='post', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        'auth.user', related_name='updated_by_user', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
