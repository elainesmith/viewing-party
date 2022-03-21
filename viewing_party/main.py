def create_movie(movie_title, genre, rating):
    new_movie = {}
    keys = ["title", "genre", "rating"]
    values = [movie_title, genre, rating]

    if None in values:
        return None
    if len(keys) == len(values):
        new_movie = dict(zip(keys, values))
        return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        for category, item in movie.items():
            if category == "title" and item == title:
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)
    return user_data

