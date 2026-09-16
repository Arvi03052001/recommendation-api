# ============================================
# core.py  -  the brain of the recommendation engine
#
# Right now: ONE function.
# We add more later, one at a time.
# ============================================


def filter_by_year(movies, year):
    """
    Take a list of movies and a year.
    Give back a list of the movies made in that year.

    This is EXACTLY your step10 task 4,
    except it keeps the whole movie instead of just the title.

        by_year -> matching_titles.append(movie["title"])   <- just the title
        this    -> result.append(movie)                     <- the whole movie

    The pattern:
        result = []
        for movie in movies:
            if ...:
                result.append(...)
        return result
    """
    # write your code here:
    result = []
    for movie in movies:
        if movie["year"] == year:
            result.append(movie)
    return result

def filter_by_rating(movies, min_rating):
    """Give back the movies rated at least min_rating."""
    # write your code here:
    result = []
    for movie in movies:
        if movie["rating"] >= min_rating:
            result.append(movie)
    return result
    