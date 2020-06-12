from movies.models import Movie, Genre
import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'junnaMovie.settings')
django.setup()


with open("dummy.csv", newline='', encoding='utf-8') as csvfile:
    data_reader = csv.reader(csvfile)
    next(data_reader)
    instances = []
    for row in data_reader:
        print(row)
        try:
            instances.append(Movie(
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
            ))
            # e(
            #     type=row[6]
            # )
        except:
            pass
    Movie.objects.bulk_create(instances)
