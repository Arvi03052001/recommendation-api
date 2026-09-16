movies = [
    {"title": "Coco",    "year": 2017},
    {"title": "Dune",    "year": 2021},
    {"title": "Get Out", "year": 2017},
]

# write a function called filter_by_year
# it takes movies and a year
# it gives back the movies from that year

def filter_by_year(movies, year):
    result = []
    for movie in movies:
        if movie["year"] == year:
            result.append(movie)
    return result

print(filter_by_year(movies, 2017))