from unittest import TestCase
from day20.GPS import GPS

class TestGPS (TestCase):
    def test_decrypt_coordinates(self):
        gps = GPS()
        input = [1, 2, -3, 3, -2, 0, 4]
        self.assertEqual([1, 2, -3, 4, 0, 3, -2], gps.decryptCoordinates(input))

    def test_get_sum_coordinates(self):
        gps = GPS()
        input = [1, 2, -3, 3, -2, 0, 4]
        dec = gps.decryptCoordinates(input)
        self.assertEqual(3, gps.getSumCoordinates(dec))

    def test_do_step_1(self):
        gps = GPS()
        input = [1, 2, -3, 3, -2, 0, 4]
        coordinates = [(i, input[i]) for i in range(len(input))]
        coordinates =  gps._doStep(coordinates, 0)
        actual_list = gps._composeListFromCoordinates(coordinates)
        self.assertEqual([2, 1, -3, 3, -2, 0, 4], actual_list)
    
    def test_do_step_2(self):
        gps = GPS()
        input = [2, 1, -3, 3, -2, 0, 4]
        coordinates = [(i, input[i]) for i in range(len(input))]
        coordinates =  gps._doStep(coordinates, 0)
        actual_list = gps._composeListFromCoordinates(coordinates)
        self.assertEqual([1, -3, 2, 3, -2, 0, 4], actual_list)

    def test_do_step_3(self):
        gps = GPS()
        input = [1, -3, 2, 3, -2, 0, 4]
        coordinates = [(i, input[i]) for i in range(len(input))]
        coordinates =  gps._doStep(coordinates, 1)
        actual_list = gps._composeListFromCoordinates(coordinates)
        self.assertEqual([1, 2, 3, -2, -3, 0, 4], actual_list)

    def test_do_step_4(self):
        gps = GPS()
        input = [1, 2, -3, 3, -2, 0, 1]
        coordinates = [(i, input[i]) for i in range(len(input))]
        coordinates =  gps._doStep(coordinates, 6)
        actual_list = gps._composeListFromCoordinates(coordinates)
        self.assertEqual([1, 1, 2, -3, 3, -2, 0], actual_list)

    def test_do_step_5(self):
        gps = GPS()
        input = [1, 2, -3, 3, -2, 0, 10]
        coordinates = [(i, input[i]) for i in range(len(input))]
        coordinates =  gps._doStep(coordinates, 6)
        actual_list = gps._composeListFromCoordinates(coordinates)
        self.assertEqual([1, 2, -3, 3, 10, -2, 0], actual_list)

    def test_do_step_6(self):
        gps = GPS()
        input = [-15, 2, -3, 3, -2, 0, 10]
        coordinates = [(i, input[i]) for i in range(len(input))]
        coordinates =  gps._doStep(coordinates, 0)
        actual_list = gps._composeListFromCoordinates(coordinates)
        self.assertEqual([2, -3, 3, -15, -2, 0, 10], actual_list)