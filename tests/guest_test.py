import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Harry", 47)

    def test_guest_has_name(self):
        self.assertEqual("Harry", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(47, self.guest.age)

    

