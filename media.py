import http.client
import json

# Class of movie objects that has all required details of movie objects


class Movie():
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.movie_title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

# function that accesses The Movie Database API to get list of currently
# popular movies and their details, except for movie trailer


def get_details():
    movies = []
    conn = http.client.HTTPSConnection("api.themoviedb.org")

    payload = "{}"

    conn.request("GET",
                 "/3/movie/popular?page=1&language=en-US&api_key=b51ba2c89c56de5c8f6b9454c20cd4ec",  # NOQA
                 payload)

    res = conn.getresponse()
    data = res.read()
    jsonStr = json.loads(data.decode("utf-8"))

    for item in jsonStr["results"]:
        movie = Movie(str(item["original_title"]),
                            "https://image.tmdb.org/t/p/w500/" + str(item["poster_path"]),  # NOQA
                            get_trailer(str(item["id"])))
        movies.append(movie)

    return movies

# function that gets the youtube trailer link from The Movie Database,
# link is not contained in details received from the other request


def get_trailer(movie_id):
    conn = http.client.HTTPSConnection("api.themoviedb.org")

    payload = "{}"

    conn.request("GET", "/3/movie/" + movie_id + "/videos?language=en-US&api_key=b51ba2c89c56de5c8f6b9454c20cd4ec",  # NOQA
                 payload)

    res = conn.getresponse()
    data = res.read()
    json_str = json.loads(data.decode("utf-8"))

    for item in json_str["results"]:
        if item["type"] == "Trailer":
            return "https://www.youtube.com/watch?v=" + item["key"]
