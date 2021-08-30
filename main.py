Menu_Prompt = "\nEnter 'a' to add a movie,'l' to see your movies, 'f' to find a movie by title, or 'q' to quit.:"
movies = []


def add_movie():
    title = input("Enter the movie title:")
    director = input("Enter the director name:")
    year = input("Enter the release year:")

    movies.append({
        "title": title,
        "director": director,
        "year": year

    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title : {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")


def find_movie():
    search_title = input("Enter the movie title you are looking for:")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
 }


def menu():

    selection = input(Menu_Prompt)
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command.Please try again")

        selection = input(Menu_Prompt)


menu()
