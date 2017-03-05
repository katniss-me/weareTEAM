from django.db import models

class Profile(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='users_Profile')
    myself = models.TextField(null=True)

    class Meta:
        ordering = ('id',)