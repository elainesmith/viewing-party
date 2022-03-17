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
    user_data["watched"] == user_data["watched"].append(movie)
    return user_data

