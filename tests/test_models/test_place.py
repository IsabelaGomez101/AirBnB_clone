#!/usr/bin/python3
""" test class Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_Place(self):
        """ test to verify that the public class attributes exist
        and verify the required type"""
        modelplace = Place()
        self.assertIs(hasattr(Place, "city_id"), True)
        self.assertAlmostEqual(type(modelplace.city_id), str)
        self.assertIs(hasattr(Place, "user_id"), True)
        self.assertAlmostEqual(type(modelplace.user_id), str)
        self.assertIs(hasattr(Place, "name"), True)
        self.assertAlmostEqual(type(modelplace.name), str)
        self.assertIs(hasattr(Place, "description"), True)
        self.assertAlmostEqual(type(modelplace.description), str)
        self.assertIs(hasattr(Place, "number_rooms"), True)
        self.assertAlmostEqual(type(modelplace.number_rooms), int)
        self.assertIs(hasattr(Place, "number_bathrooms"), True)
        self.assertAlmostEqual(type(modelplace.number_bathrooms), int)
        self.assertIs(hasattr(Place, "max_guest"), True)
        self.assertAlmostEqual(type(modelplace.max_guest), int)
        self.assertIs(hasattr(Place, "price_by_night"), True)
        self.assertAlmostEqual(type(modelplace.price_by_night), int)
        self.assertIs(hasattr(Place, "latitude"), True)
        self.assertAlmostEqual(type(modelplace.latitude), float)
        self.assertIs(hasattr(Place, "longitude"), True)
        self.assertAlmostEqual(type(modelplace.longitude), float)
        self.assertIs(hasattr(Place, "amenity_ids"), True)
        self.assertAlmostEqual(type(modelplace.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
