# PPHA 30535
# Spring 2021
# Homework 3

# RIMJHIM AGRAWAL

# RIMJHIM
# RIMJHIMCODES

# Due date: Sunday April 24th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Begin with the class below and do the following:
#   a) Modify the what_to_watch method so that it takes an optional keyword
#       argument that allows the user to narrow down the random selection by
#       category (e.g. select only from movies with category 'action'), but
#       defaults to the entire list of titles as it does now.
#   b) The what_to_watch method currently raises a ValueError if you use it
#       before entering any movies. Modify it using try/except so that it tells
#       the user what they did wrong instead of raising an error.
#   c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.
#   d) Override the add_movie method in your new class so that if it is called
#       without arguments, it instead asks for user input to add a title/year/
#       category/stars, but if it is called with arguments it behaves as before
#   e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
#       input, so that they can't enter something that makes no sense (e.g. title=None
#       or year='dog')
#   f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
#       returns a list of all the titles in the database currently, ordered
#       highest ranking (by stars) to lowest
#
# NOTE: Your final submission should have only TWO classes: one (modified)
#       MovieDataBase, and the new InteractiveMovieDataBase

from numpy import random

class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}

    def add_movie(self, title, year, category, stars):
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'stars':stars}
        print(f'{title} ({year}) added to the database.')

    def what_to_watch(self, **category):
        try:
            choice = random.choice(self.titles)
            movie = self.movies[choice]
            print(f"Your movie today is {choice} ({movie['year']}),"
                  " which is a {movie['category']}, and was given {movie['stars']} stars.")
        except ValueError:
            print("No movies to choose from. Please add movies.")
            
            
class InteractiveMovieDataBase(MovieDataBase):
    def add_movie(self, *data):
        try:
            super(InteractiveMovieDataBase, self).add_movie(*data)
        except:
            title, year, category = input('Enter movie title, year and '
                                          'category in order: ').split(",")
            assert(isinstance(title, str)), 'Title needs to be a string.'
            assert(year.isdigit()), 'Year has to be a number.'
            assert(category in ('action', 'animation', 
                                'comedy', 'drama', 'fantasy', 'horror', 
                                'romance')), 'Please choose a valid category'
            
            stars = float(input('Enter stars: '))
            assert stars <= 5 and stars >= 0, 'Enter valid rating'
            
            self.titles.append(title)
            self.movies[title] = {'year':year, 'category':category, 'stars':stars}
            
            print(f'{title} ({year}) added to the database.')
        
    def movie_rankings(self):
        #ranking = {self.titles: self.movies[k] for k in self.movies.keys() & {'stars'}}
        ranking = [sorted(self.titles, key=lambda kv: self.movies[kv]['stars'], reverse=True)]
        return ranking
 
mov1 = MovieDataBase()       
mov1.add_movie("Taken", 2008, 'action', 4) 
mov1.add_movie("Jab We Met", 2003, 'romance', 4)
mov1.add_movie("Orphan", 2010, 'horror', 3)   
mov1.what_to_watch()

mov2 = MovieDataBase()
mov2.what_to_watch()

#[Baahubali, 2015, fantasy, 5]
#[Kimi No Na Wa,2017,animation, 4.6]
#[Main Hoon Na,2004,drama, 3.8]
#[X-Men, 2011, sci-fi, 4]

mov3 = InteractiveMovieDataBase()
mov3.add_movie("Baahubali", 2015, 'fantasy', 5)
mov3.add_movie("Kimi No Na Wa", 2017, 'animation', 3.6)
mov3.add_movie("Masaan", 2019, 'drama', 4.7)
mov3.add_movie()  #Run 3-4 times
mov3.movie_rankings()

mov4 = InteractiveMovieDataBase()
mov4.add_movie("Taken", 2008, 'action', 4)

# Ref: https://www.geeksforgeeks.org/python-dictionary/
# Ref: https://www.geeksforgeeks.org/python-super/
# Ref: https://stackoverflow.com/questions/25320595/python-how-to-override-a-class-method-while-preserving-decorators-and-calling
# Ref: https://stackoverflow.com/questions/4110665/sort-nested-dictionary-by-value-and-remainder-by-another-value-in-python