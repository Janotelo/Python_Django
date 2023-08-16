from django.db import models

# Create your models here.

### *This are Django Function where it converts  ###
### python command to sql commands               ###
### *Can look for 'django model field reference' ###
### *Don't use reserved names                    ###
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = 