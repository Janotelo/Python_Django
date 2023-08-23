from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.

### *This are Django Function where it converts  ###
### python command to sql commands               ###
### *Can look for 'django model field reference' ###
### *Don't use reserved names                    ###
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    

    def __str__(self):
        return f"{self.title} ({self.rating})"