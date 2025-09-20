def Divider():
    print("\n------------------------\t------------------------\n")
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __repr__(self):
        return "Book('{}' , '{}' , '{}')".format(self.title , self.author , self.isbn)
    def __str__(self):
        return "Book : {}".format(self.title)
    

book1 = Book("PythonBasicsDoc", "Yousef","958-412-852-952-5")
book2 = Book("Rasael min alquraan","Adham Sharqawy", "123-147-789-963-5")

print(book1)
print(repr(book2))

Divider()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Vector({},{})".format(self.x,self.y)
    def __add__(self, other):
        newX = self.x + other.x
        newY = self.y + other.y
        return Vector(newX,newY)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
v1 = Vector(2,3)
v2 = Vector(4,6)
v3 = Vector(6,9)

v4 = v1 + v2
print(v4)
print(v3 == v4)


Divider()

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song_title):
        self.songs.append(song_title)
    def __len__(self):
        return len(self.songs)
    def __getitem__(self, index):
        return self.songs[index]
    def __str__(self):
        return "Playlist : {}, Songs : {}".format(self.name , len(self))

rock_playlist = Playlist("Rock Playlist")
rock_playlist.add_song("Asly Falastini")
rock_playlist.add_song("meraba")
rock_playlist.add_song("ya masr")
print(len(rock_playlist))
print(rock_playlist[1])
print(rock_playlist)
