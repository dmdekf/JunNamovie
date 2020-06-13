from movies.models import Movie, Genre
import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'junnaMovie.settings')
django.setup()


with open("dummy.csv", newline='', encoding='utf-8') as csvfile:
    data_reader = csv.reader(csvfile)
    next(data_reader)
    instance = []
    for row in data_reader:

        try:
            instance.append(Movie(
                title=row[0],
                popularity=row[1],
                release=row[2],
                poster_URL=row[3],
                backdrop_URL=row[4],
                adult=row[5],
                genres=row[6],
                overview=row[7],
                runtime=row[8],
                status=row[9],
                tagline=row[10],
                vote_aver=row[11],
                vote_count=row[12],
            ))
        except:
            pass
    Movie.objects.bulk_create(instance)

    print(1111111111)
    genre_idx = [(28, "Action"),
                 (12, "Adventure"),
                 (16, "Animation"),
                 (35, "Comedy"),
                 (80, "Crime"),
                 (99, "Documentary"),
                 (18, "Drama"),
                 (10751, "Family"),
                 (14, "Fantasy"),
                 (36, "History"),
                 (27, "Horror"),
                 (10402, "Music"),
                 (9648, "Mystery"),
                 (10749, "Romance"),
                 (878, "Science Fiction"),
                 (10770, "TV Movie"),
                 (53, "Thriller"),
                 (10752, "War"),
                 (37, "Western")]
    instance = []
    for idx_code, idx_type in genre_idx:
        try:
            instance.append(Genre(
                code=idx_code,
                type=idx_type,
            ))
        except:
            pass
    Genre.objects.bulk_create(instance)

    movies = Movie.objects.all()
    for movie in movies:
        print(movie)
        temp = movie.genres  # movie.genres = "[51, 12]"
        temp = temp.replace("[", "").replace("]", "")
        temp = list(map(int, temp.split(",")))  # temp =[51,12]
        if temp:
            for g in temp:  # g = 51
                g_ob = Genre.objects.get(code=g)
                print(g_ob)
                movie.gen.add(g_ob)  # gen이 manytomany 설정한거
