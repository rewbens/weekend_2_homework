import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Caraoke rocks")
       
    def test_room_has_name(self):
        self.assertEqual("Caraoke rocks", self.room.name)

    def test_room_has_guests(self):
        self.assertEqual([], self.room.guests)

    def test_room_can_add_guest(self):
        guest_1 = Guest("Ellie", 24)
        # guest_2 = Guest("Norman", 36)
        # guest_3 = Guest("Alice", 29)
        self.room.add_guest(guest_1)
        self.assertEqual([guest_1], self.room.guests)


    def test_room_has_songs(self):
        self.assertEqual([], self.room.songs)

    def test_room_can_add_song(self):
        song_1 = Song("Friday Im in Love", "The Cure", "Rock")
        # song_2 = Song("smile", "Wolf Alice", "Alt Rock")
        # song_3 = Song("Papa New Guinea", "Future Sound of London", "Dance")
        self.room.add_song(song_1)
        self.assertEqual([song_1], self.room.songs)

    # def test_room_can_remove_guest(self):
        # guest_1 = Guest("Ellie", 24)
        # self.room.add_guest(guest_1)
        # self.room.remove_guest(guest_1)
        # self.assertEqual([guest_1], self.room.guests)

    