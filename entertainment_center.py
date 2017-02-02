# This file creates a list of movies and series using the appropriate classes
# defined in media.py and fills in the information necessary for each of
# these classes. It then calls a function called fresh_tomatoes.open_movies_page()
# from fresh_tomatoes.py to create a webpage that shows the movies and the
# series and the information on them.
# In case you hover above the poster of a movie and left-click it will show the
# Trailer of the movie. In case you hover above the name of a season
# of a series and left-click it will show either the Trailer or the Intro of
# that season.

import media
import fresh_tomatoes

moon = media.Movie("Moon",
                        "A story about a man who experiences a personal crisis as he nears the end of a three-year solitary stint mining helium-3 on the far side of the Moon",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Moon_%282008%29_film_poster.jpg",
                        "https://www.youtube.com/watch?v=Cb3exxD2nGo")


arrival=media.Movie("Arrival",
                        "A story about an alien species coming to earth and the attempt to find a way to communicate with them",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
                        "https://www.youtube.com/watch?v=PkH_eDfOkcU")

myseason1=media.Season("Season1","https://www.youtube.com/watch?v=Gdi50ZJnE9Y")
myseason2=media.Season("Season2","https://www.youtube.com/watch?v=U8R2eLeiUYE")
myseason3=media.Season("Season3","https://www.youtube.com/watch?v=195O4VUA8MM")
myseason4=media.Season("Season4","https://www.youtube.com/watch?v=qfEPQqHx40c")
myseason5=media.Season("Season5","https://www.youtube.com/watch?v=UOiSjoek-5Q")
myseason6=media.Season("Season6","https://www.youtube.com/watch?v=9vIsQ25Krq8")
myseason7=media.Season("Season7","https://www.youtube.com/watch?v=EbmLE9GFMwU")
myseason8=media.Season("Season8","https://www.youtube.com/watch?v=dIawFeVDa6k")
myseason9=media.Season("Season9","https://www.youtube.com/watch?v=fi3nJBlJs48")
mylist=[myseason1,myseason2,myseason3,myseason4,myseason5,myseason6,myseason7,myseason8,myseason9]
dr_who=media.Series("Dr. Who",
                        "The adventures of a Time Lord travelling through time and space in a blue police box",
                        "https://upload.wikimedia.org/wikipedia/en/0/05/Doctor_Who_-_Current_Titlecard.png",
                        mylist)

myseason1=media.Season("Season1","https://www.youtube.com/watch?v=BtrUhIuEqdY")
myseason2=media.Season("Season2","https://www.youtube.com/watch?v=Bhc_Oem8Whc")
myseason3=media.Season("Season3","https://www.youtube.com/watch?v=d9EbGd1AlMg")
myseason4=media.Season("Season4","https://www.youtube.com/watch?v=2w560Q8ELOg")
myseason5=media.Season("Season5","https://www.youtube.com/watch?v=2w560Q8ELOg")
mylist=[myseason1,myseason2,myseason3,myseason4,myseason5]

bab5=media.Series("Babylon 5",
                          "The story of a space station",
                          "https://upload.wikimedia.org/wikipedia/en/9/9d/Smb5-s4.jpg",
                          mylist)
                        
         
movies = [moon,arrival,dr_who,bab5]
fresh_tomatoes.open_movies_page(movies)
