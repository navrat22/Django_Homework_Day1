from email.policy import default

from django.db import models


GENRE_TYPES = (
    (-0, "not defined"),
    (0, "rock"),
    (1, "metal"),
    (2, "pop"),
    (3, "hip-hop"),
    (4, "electronic"),
    (5, "reggae"),
    (6, "other")
)
STATUS_TYPES = (
    (1, "in writing"),
    (2, "pending editor approval"),
    (3, "published")
)

STARS = (
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)

)



class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices = GENRE_TYPES,default=-1)

    def __str__(self):
        return f"{self.name} - {self.year}"


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)

class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices = STATUS_TYPES)
    published = models.DateField(null=True)
    removal_date = models.BooleanField(null=False)


class Album(models.Model):
    album_title =models.CharField(max_length=128)
    release_year = models.IntegerField(null=True)
    rating = models.IntegerField(choices = STARS)






