# imdb-django-RESTful-Api
imdb like django RESTApi to fetch movie data

this is a imdb like RESTApi to fetch the movie details developed using django rest framework

requirements:

python 3.7 django 2.2.8 djangorestframework

AT first make the migrations using python manage.py makemigrations

then run python manage.py migrate

after this the migrations are created and then

dump the initial data into the sqlite3 database using the command python manage.py insert_data_to_db
this will run the django custom admin command and will dump the json data into the database

to run the Api run the command python manage.py runserver

then go to http://127.0.0.1/movies

to view the movies

create the superuser

and go to http://127.0.0.1/admin

to login into the admin panel

the superuser will have the permission to insert, edit and delete this data
