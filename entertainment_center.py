"""
This porject dynamically generates a webpage of my favourite movies
from Python data structures.
"""

import media
import crisp_tomatoes

''' Creating instances of the class Movie defined in media '''
sherlock = media.Movie("Sherlock(TV)",
                       "A modern update finds the famous sleuth and his doctor"
                       "partner solving crime in 21st century London.",
                       "https://images-na.ssl-images-amazon.com/images/I/"
                       "41QuZEvMpdL."
                       "_AC_UL320_SR214,320_.jpg",
                       "https://www.youtube.com/watch?v=lAai7yjv6v4")

vForVendetta = media.Movie("v for vendetta",
                           "In a future British tyranny, a shadowy freedom"
                           " fighter,known only by the alias of 'V', plots"
                           "to overthrow it with the help of a young woman.",
                           "https://i.pinimg.com/originals/d5/a7/87/"
                           "d5a787c7e5bcafb46677a5f04734d078.jpg",
                           "https://www.youtube.com/watch?v=KKvvOFIHs4k")

pink = media.Movie("Pink",
                   "When three young women are implicated in a crime,"
                   "a retired lawyer steps forward to help them clear"
                   "their names.",
                   "https://shyfyy.files.wordpress.com/2016/08/pink-1.jpg",
                   "https://www.youtube.com/watch?v=AL2TShb6fFs")

penguinsOfMadagascar = media.Movie("Penguins of Madagascar",
                                   "Skipper, K owalski, Rico and Private join"
                                   "forces with undercover organization The "
                                   "North Wind to stop the villainous"
                                   "Dr. Octavius Brine from destroying the"
                                   " world as we know it.",
                                   "http://www.impawards.com/2014/posters/"
                                   "penguins_of_madagascar_xlg.jpg",
                                   "https://www.youtube.com/watch?v=AWxy9C5"
                                   "svFU"
                                   )

gangsOfWasseypur = media.Movie("Gangs of Wasseypur",
                               "A clash between Sultan and Shahid Khan leads"
                               " to the expulsion of Khan from Wasseypur,"
                               " and ignites a deadly blood feud spanning"
                               " three generations.",
                               "https://upload.wikimedia.org/wikipedia/en/6/"
                               "6a/Gangs_of_Wasseypur_poster.jpg",
                               "https://www.youtube.com/watch?v=j-AkWDkXcMY")

shawshankRedemption = media.Movie("The Shawshank Redemption",
                                  "Two imprisoned men bond over a number of"
                                  " years,finding solace and eventual"
                                  " redemption through acts of common decency",
                                  "https://www.movieruntime.com/wp-content/"
                                  "uploads/2017/09/9O7gLzmreU0nGkIB6K3BsJbz"
                                  "vNv.jpg",
                                  "https://www.youtube.com/watch?v=NmzuHjWm"
                                  "XOc")

''' Creating a list of all movie instances '''
movies_list = [sherlock, vForVendetta, pink,
               penguinsOfMadagascar, gangsOfWasseypur, shawshankRedemption]

''' Passing list to the function open_movies_page() of the 'crisp_tomatoes'
    which would populate the website with these instances '''
crisp_tomatoes.open_movies_page(movies_list)
