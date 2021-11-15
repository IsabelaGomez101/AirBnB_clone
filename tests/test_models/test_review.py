#!/usr/bin/python3
""" test class Review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_review(self):
        """ test to verify that the public class attributes exist
        and verify the required type"""
        modelreview = Review()
        self.assertIs(hasattr(Review, "place_id"), True)
        self.assertAlmostEqual(type(modelreview.place_id), str)
        self.assertIs(hasattr(Review, "user_id"), True)
        self.assertAlmostEqual(type(modelreview.user_id), str)
        self.assertIs(hasattr(Review, "text"), True)
        self.assertAlmostEqual(type(modelreview.text), str)


if __name__ == '__main__':
    unittest.main()
