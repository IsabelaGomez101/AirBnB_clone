#!/usr/bin/python3
""" test class BaseModel"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_docstrings(self):
        self.assertIs(hasattr(BaseModel, "__init__"), True)
        self.assertIs(hasattr(BaseModel, "save"), True)
        self.assertIs(hasattr(BaseModel, "__str__"), True)

    def test_BaseModel(self):
        model1 = BaseModel()
        self.assertAlmostEqual(type(model1.id), str)
        self.assertAlmostEqual(len(model1.id), 36)

if __name__ == "__main__":
    unittest.main()