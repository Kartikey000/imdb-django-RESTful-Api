from rest_framework import serializers
from .models import Director, Genre, Movie

class GenreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = "__all__"

class DirectorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Director
		fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):

	genre = GenreSerializer(many=True)
	director = DirectorSerializer(many=True)
	class Meta:
		model = Movie
		fields = ('name','director','popularity','imdb_score','genre')