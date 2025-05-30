from django.db import models
from django.utils.text import slugify


class Actors(models.Model):
    name = models.CharField(max_length=55)
    addres = models.CharField(max_length=100)
    birth_day = models.DateField()




class Movie(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True,null=True)
    year = models.IntegerField(default=1900)
    actors = models.ManyToManyField(Actors,related_name='actors')
    genre = models.TextField()

    def save(self,**kwargs):
        if not self.slug:
            orign_slug = slugify(self.title)
            slug = orign_slug
            count = 0
            while Movie.objects.filter(slug=slug).exists():
                slug = f"{slug}-{count}"
                count += 1
            self.slug = slug
        super().save(**kwargs)
    def __str__(self):
        return self.title


