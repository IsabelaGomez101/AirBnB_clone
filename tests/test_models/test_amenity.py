#!/usr/bin/python3
""" test class Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity(self):
        """ test to verify that the public class attributes exist
        and verify the required type"""
        modelamenity = Amenity()
        self.assertIs(hasattr(Amenity, "name"), True)
        self.assertAlmostEqual(type(modelamenity.name), str)


if __name__ == '__main__':
    unittest.main()
