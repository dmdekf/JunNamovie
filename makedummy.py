import requests
import time
from datetime import datetime, timedelta
import csv
from collections import OrderedDict

# csv 파일 생성을 위한 함수 입니다. 각각 파일명, wirte ///
with open('dummy.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['title', 'popularity', 'release', 'poster_URL', 'backdrop_URL', 'adult',
                  'genres', 'overview', 'runtime', 'status', 'tagline', 'vote_aver', 'vote_count']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    # file_data = OrderedDict()

    API_KEY = '2c07b9f6a977110648eb9cc6b745c51b'

    for i in range(100, 105):

        URL = f'https://api.themoviedb.org/3/movie/{i}?api_key={API_KEY}'
        data = requests.get(URL).json()

        # file_data = OrderedDict()
        file_data = {}
        try:
            file_data['title'] = data["original_title"]
            file_data['popularity'] = data["popularity"]
            file_data['release'] = data["release_date"]
            file_data['poster_URL'] = data["poster_path"]
            file_data['backdrop_URL'] = data["backdrop_path"]
            file_data['adult'] = data["adult"]
            # result["genres"] = data["genres"]
            file_data['genres'] = []
            for genre in data["genres"]:
                file_data["genres"].append(genre["id"])
            file_data['overview'] = data["overview"]
            file_data['runtime'] = data["runtime"]
            # file_data['status'] = data["status"]
            if data["status"] == "Released":
                file_data['status'] = True
            else:
                file_data['status'] = False
            file_data['tagline'] = data["tagline"]
            file_data['vote_aver'] = data["vote_average"]
            file_data['vote_count'] = data["vote_count"]
            writer.writerow(file_data)
        except KeyError:
            pass
        # print(json.dumps(file_data, ensure_ascii=False,indent="\t"))
        # json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
        # make_file.write(",\n")
