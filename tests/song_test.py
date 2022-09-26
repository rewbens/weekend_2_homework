import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Hey Jude", "Beatles", "rock n roll")
       
    def test_song_has_title(self):
        self.assertEqual("Hey Jude", self.song.title)

    def test_song_has_band(self):
        self.assertEqual("Beatles", self.song.band)

    def test_song_has_genre(self):
        self.assertEqual("rock n roll", self.song.genre)