#!/usr/bin/python3
""" test class City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_city(self):
        """ test to verify that the public class attributes exist
        and verify the required type"""
        modelcity = City()
        self.assertIs(hasattr(City, "name"), True)
        self.assertAlmostEqual(type(modelcity.name), str)
        self.assertIs(hasattr(City, "state_id"), True)
        self.assertAlmostEqual(type(modelcity.state_id), str)


if __name__ == '__main__':
    unittest.main()
