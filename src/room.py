class Room:

    def __init__(self, name):
        self.name = name
        self.songs = []
        self.guests = []
    

    def add_guest(self, guests):
        self.guests.append(guests)

    def add_song(self, songs):
        self.songs.append(songs)

    def remove_guest(self, guests):
        self.guests.remove(guests)





