from django.db import models

# Create your models here.


class Genre(models.Model):
	genre_name= models.CharField(max_length=200)

	def __str__(self):
		return self.genre_name

class Director(models.Model):
	director_name= models.CharField(max_length=200)

	def __str__(self):
		return self.director_name

class Movie(models.Model):
	name = models.CharField(max_length=200)
	director = models.ManyToManyField(Director)
	popularity = models.FloatField()
	imdb_score = models.FloatField()
	genre = models.ManyToManyField(Genre)

	def __str__(self):
		return self.name


