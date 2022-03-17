
def create_movie(movie_title, genre, rating):
    new_movie = {}
    keys = ["title", "genre", "rating"]
    values = [movie_title, genre, rating]
    valid_input = False

    if len(keys) == len(values):
        valid_input = True
        new_movie = dict(zip(keys, values))
        return new_movie
    while not valid_input:
        return None