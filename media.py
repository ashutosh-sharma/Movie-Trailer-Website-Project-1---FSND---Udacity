"""
This file contains class Movie which would be used
to create movie instances in entertainment_center.py
"""
import webbrowser


class Movie():
    '''
    class Movie has members:
        movie_title: Name of the Movie
        stroyline: Storyline of the movie
        poster URL: URL of the poster of the movie
        trailer URL: Youtube URL of the trailer of the movie
    '''
    # Constructor, which accept all data members as arguments
    def __init__(self, movie_title, storyline, poster_image, trailer_URL):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_URL

    ''' Member funciton of class Movie- to open the youtube trailer
        in the webbrower '''
    # Using inbuilt python package 'webbrowser'
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_URL)
