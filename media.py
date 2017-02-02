# Lesson 3.4: Make Classes
# Mini-Project: Movies Website


class Video():
    """ Class Video serves as a class to store the title, the poster_image_url and
    the content of video file"""
    def __init__(self,title,content,poster):
        self.title=title
        self.poster_image_url=poster
        self.content=content
    
class Movie(Video):
    """Class Movie inherits from class Video. It serves as a class to additionally
    store the trailer_youtube_url of a movie."""
    def __init__(self,title,content,poster,trailer):
        Video.__init__(self,title,content,poster)
        self.trailer_youtube_url=trailer

class Season():
    """Class Season contains the title and the trailer_youtube_url of a single
    season of a series."""
    def __init__(self,title,trailer):
        self.title=title
        self.trailer_youtube_url=trailer

class Series(Video):
    """Class Series inherits from class Video. It additionally stores a list
    of seasons of a series (season_list) where each season is of class Season."""
    def __init__(self,title,content, poster,season_list):
         Video.__init__(self, title,content,poster)
         self.season_list=season_list
    
        
