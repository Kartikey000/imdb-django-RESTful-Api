from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from ...models import Director, Genre, Movie

import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        filepath = settings.BASE_DIR + '/moviedata.json'
        with open(filepath, 'r') as file:
            file_data = file.read()
            data = json.loads(file_data)
            li = {}
            for movie_item in data:
                li['name'] = movie_item.get('name')
                li['popularity'] = movie_item.get('popularity')
                #li['director'] = movie_item.get('director')
                li['imdb_score'] = movie_item.get('imdb_score')
                ob, created = Movie.objects.get_or_create(**li)

                #creating director_name
                director_n = movie_item.get('director')
                obd, created = Director.objects.get_or_create(director_name=director_n)
                #adding director_name to the Movie object
                ob.director.add(obd)
                #obm = Movie.objects.create(**li)
                genre_list = movie_item.get('genre')
            
                # create genre for each genre in list and attach to current movie
                for name in genre_list:
                    obg, created = Genre.objects.get_or_create(genre_name=name)
                    ob.genre.add(obg)
                    ob.save()
                    print("success")
                    """ q=Genre.objects.get(genre_name=name)
                    if q==1:
                        obm.Genre.add(q)
                    else:
                        obg = Genre.objects.create(genre_name=genre_name)
                        obm.genre.add(obg) """
