#!/usr/bin/python3
""" test class User"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_Amenity(self):
        """ test to verify that the public class attributes exist
        and verify the required type"""
    modelAmenity = Amenity()


if __name__ == '__main__':
    unittest.main()
