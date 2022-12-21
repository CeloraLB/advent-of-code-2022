from unittest import TestCase
from day20.GPS import GPS

class TestHillClimber (TestCase):
    def test_decrypt_coordinates(self):
        gps = GPS()
        input = [1, 2, -3, 3, -2, 0, 4]
        self.assertEqual([1, 2, -3, 4, 0, 3, -2], gps.decryptCoordinates(input))

    def test_get_sum_coordinates(self):
        gps = GPS()
        input = [1, 2, -3, 3, -2, 0, 4]
        dec = gps.decryptCoordinates(input)
        self.assertEqual(3, gps.getSumCoordinates(dec))