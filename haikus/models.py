import uuid
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models
from django.urls import reverse


class Haiku(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    poem = models.CharField('はいく', max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
    )
    description = models.TextField('せつめい', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField('イメージ', upload_to='images/', blank=True)

    def __str__(self):
        return self.poem
    
    def get_absolute_url(self):
        return reverse('haiku_detail', kwargs={'pk': str(self.pk)})


class Review(models.Model):
    haiku = models.ForeignKey(
        Haiku,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.review