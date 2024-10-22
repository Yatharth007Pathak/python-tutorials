# Movie information using python

import imdb

# Create an instance of the IMDb class
ia = imdb.Cinemagoer()

# Take input for the movie name
Movie = input("Enter a movie name: ") 
items = ia.search_movie(Movie)

# Print search results
print("\nSearch results:")

# Display the movie results
for index, movie in enumerate(items):
    title = movie.get('title', 'N/A')  # Get title, default to 'N/A' if not found
    year = movie.get('year', 'N/A')    # Get year, default to 'N/A' if not found
    print(f"{index + 1}. {title} ({year})")


# Ask the user to select a movie by its index
movie_index = int(input("\nEnter the number of the movie you want to get info for: ")) - 1

# Get the selected movie's ID
movie_id = items[movie_index].movieID

# Fetch detailed movie info using the movie ID
movie_info = ia.get_movie(movie_id)

# Print detailed movie information
print("\nMovie Information:")

# Display various details about the movie
print(f"Title: {movie_info.get('title')}")
print(f"Year: {movie_info.get('year')}")
print(f"Rating: {movie_info.get('rating')}")
print(f"Genres: {', '.join(movie_info.get('genres', []))}")
print(f"Director(s): {', '.join(str(d) for d in movie_info.get('directors', []))}")
print(f"Cast: {', '.join(str(c) for c in movie_info.get('cast', [])[:5])}...")
print(f"Plot: {movie_info.get('plot outline')}")
print(f"Runtime: {movie_info.get('runtimes', ['N/A'])[0]} minutes")
print(f"Country: {', '.join(movie_info.get('countries', []))}")
print(f"Language: {', '.join(movie_info.get('languages', []))}")
   

'''
To use the imdb package in your Python environment, you'll need to install the IMDbPY library, which allows you to access data from IMDb.

IMDbPY is a Python package that allows you to access and manipulate data from the Internet Movie Database (IMDb). 
It provides tools for retrieving information about movies, actors, and other related data, 
making it useful for various applications such as data analysis, web development, and personal projects related to films.

Key Features
Access to IMDb Data: Fetch information on movies, actors, directors, and more.
Search Functionality: Perform searches for movies or people by title or name.
Data Extraction: Extract detailed data including ratings, reviews, and box office information.
Custom Queries: Create custom queries to get specific information.
Local Database Support: Option to use a local database instead of fetching data from the web.

Installation
You can install IMDbPY using pip:
pip install IMDbPY
'''


'''
Here's a line-by-line breakdown of the provided code:

import imdb
This line imports the imdb module, which provides access to the IMDb database for retrieving movie information.

ia = imdb.Cinemagoer()
An instance of the Cinemagoer class is created and assigned to the variable ia. This instance will be used to interact with the IMDb database.

Movie = input("Enter a movie name: ")
This line prompts the user to enter a movie name and stores the input in the variable Movie.

items = ia.search_movie(Movie)
The search_movie method of the Cinemagoer instance ia is called with the movie name provided by the user. 
The results are stored in the variable items, which is a list of movies matching the search query.

print("\nSearch results:")
This line prints a header for the search results, starting a new line.

for index, movie in enumerate(items):
A loop is initiated to iterate over the items list. 
The enumerate function is used to get both the index (position) and the movie object from the list.

title = movie.get('title', 'N/A')
The title of the movie is retrieved using the get method. If the title is not found, it defaults to 'N/A' (not available).

year = movie.get('year', 'N/A')
Similarly, the release year of the movie is retrieved, defaulting to 'N/A' if not found.

print(f"{index + 1}. {title} ({year})")
This line prints the index (incremented by 1 for user-friendliness), the movie title, and the year in a formatted string.

movie_index = int(input("\nEnter the number of the movie you want to get info for: ")) - 1
The user is prompted to enter the index of the movie for which they want more information. 
The input is converted to an integer and decremented by 1 to match Python's zero-based indexing.

movie_id = items[movie_index].movieID
The movieID of the selected movie is obtained from the items list using the movie_index.

movie_info = ia.get_movie(movie_id)
Detailed information about the selected movie is fetched using the get_movie method of the Cinemagoer instance, passing in the movie_id. 
The result is stored in the movie_info variable.

print("\nMovie Information:")
This line prints a header for the detailed movie information, starting a new line.

print(f"Title: {movie_info.get('title')}")
The title of the movie is printed, retrieved from movie_info.

print(f"Year: {movie_info.get('year')}")
The release year of the movie is printed.

print(f"Rating: {movie_info.get('rating')}")
The movie's rating is printed.

print(f"Genres: {', '.join(movie_info.get('genres', []))}")
The genres of the movie are printed, joined into a string. If no genres are found, it defaults to an empty list.

print(f"Director(s): {', '.join(str(d) for d in movie_info.get('directors', []))}")
This line prints the directors of the movie, converted to strings and joined into a single string. 
Defaults to an empty list if no directors are found.

print(f"Cast: {', '.join(str(c) for c in movie_info.get('cast', [])[:5])}...")
The first five cast members are printed, joined into a string. If no cast is found, it defaults to an empty list.

print(f"Plot: {movie_info.get('plot outline')}")
The plot outline of the movie is printed.

print(f"Runtime: {movie_info.get('runtimes', ['N/A'])[0]} minutes")
The runtime of the movie is printed. If no runtime is found, it defaults to 'N/A'.

print(f"Country: {', '.join(movie_info.get('countries', []))}")
The countries where the movie was produced are printed, joined into a string.

print(f"Language: {', '.join(movie_info.get('languages', []))}")
The languages in which the movie was made are printed, joined into a string.

This code allows a user to search for a movie by name and retrieve detailed information about it, including title, year, 
rating, genres, directors, cast, plot, runtime, country, and language.
'''