import media
import fresh_tomatoes

# runs function in the media module to use The Movie Database API to get
# list of current popular movies and their details to display
movies = media.get_details()

fresh_tomatoes.open_movies_page(movies)
