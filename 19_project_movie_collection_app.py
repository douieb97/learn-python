





menu = """
a - Add a new movie
s - Show movies list
f - Find a movie by title
q - Quit
"""

choice = input('Please enter your choice: ')
movies = []

def find(title):
    for movie in movies:
        if title == movie['title']:
            print(f'title: {movie["title"]}, director: {movie["director"]}, release year: {movie["release"]}')
        

while choice != 'q':
    if choice == 'a':
        title = input('Enter movie title: ')
        director = input('Enter movie director: ')
        release = input('Enter movie release year: ')
        movies.append({
            "title": title,
            "director": director,
            "release": release,
        })
    if choice == 's':
        for movie in movies:
            print(f'title: {movie["title"]}, director: {movie["director"]}, release year: {movie["release"]}')
    if choice == 'f':
        pass
    print(menu)
    choice = input('Please enter your choice: ')


"""
user
    all movies
    my movies
    find my title

show menu

movie: title, director, release year
"""
