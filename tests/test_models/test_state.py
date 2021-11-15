#!/usr/bin/python3
""" test class State"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state(self):
        """ test to verify that the public class attributes exist
        and verify the required type"""
        modelstate = State()
        self.assertIs(hasattr(State, "name"), True)
        self.assertAlmostEqual(type(modelstate.name), str)


if __name__ == '__main__':
    unittest.main()
