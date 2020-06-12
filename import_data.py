import csv 
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'junnaMovie.settings')
django.setup()

from movies.models import Movie, Genre

with open("../dummy.csv", newline='', encoding='utf-8') as csvfile:
            data_reader = csv.reader(csvfile)
            next(data_reader)
            for row in data_reader:
                try:
                    Movie.objects.create(
                        title=row[0],
                        popularity=row[1],
                        release=row[2],
                        poster_URL=row[3],
                        backdrop_URL=row[4],
                        adult=row[5],
                        overview=row[7],
                        runtime=row[8],
                        status=row[9],
                        tagline=row[10],
                        vote_aver=row[11],
                        vote_count=row[12],
                    )
                    Genre.objects.create(
                        type=row[6]
                    )
                except:
                    pass