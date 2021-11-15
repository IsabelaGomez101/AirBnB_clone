#!/usr/bin/python3
""" test class User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_User(self):
        """ test to verify that the public class attributes exist
        and verify the required type"""
        modeluser = User()
        self.assertIs(hasattr(User, "email"), True)
        self.assertAlmostEqual(type(modeluser.email), str)
        self.assertIs(hasattr(User, "password"), True)
        self.assertAlmostEqual(type(modeluser.password), str)
        self.assertIs(hasattr(User, "first_name"), True)
        self.assertAlmostEqual(type(modeluser.first_name), str)
        self.assertIs(hasattr(User, "last_name"), True)
        self.assertAlmostEqual(type(modeluser.last_name), str)


if __name__ == '__main__':
    unittest.main()
