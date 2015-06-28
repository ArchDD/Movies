# -*- coding: cp1252 -*-
import fresh_tomatoes
import media

# create a list to hold movies
movie_list = []


# function that initialises movies and add them to list
def extend_movie_list(movie_title, movie_storyline, poster_image,
                      trailer_youtube):
    movie = media.Movie(movie_title, movie_storyline, poster_image,
                        trailer_youtube)
    movie_list.extend([movie])

# extending movie list
extend_movie_list("Jurassic World",
                  "Genetically modified frog goes crazy",
                  "http://www.fatmovieguy.com/wp-content/uploads/2015/04/Jurassic-World-Movie-Poster-3-Chris-Pratt-Raptors.jpg",
                  "https://www.youtube.com/watch?v=RFinNxS5KN4")

extend_movie_list("Pokemon: The Movie 2000",
                  "Ash meets a pokemon called Lugia",
                  "http://upload.wikimedia.org/wikipedia/fi/2/27/Pokemon-the-movie-2000-poster.jpg",
                  "www.youtube.com/watch?v=NrYGPtEhkVQ")

extend_movie_list("Evangelion: 3.0 You Can (Not) Redo",
                  "A story of a mad man",
                  "http://m.mhcdn.net/store/spoiler/20121025/1351149118.jpg",
                  "www.youtube.com/watch?v=Ua75H0k7-N0")

# passing the list of instances to fresh_tomatoes
fresh_tomatoes.open_movies_page(movie_list)
