# -*- coding: utf-8 -*-
import unittest 


class MyTests(unittest.TestCase):

    def setUp(self):
        """runs before test"""
        
    def tearDown(self):
        """runs after test """

    def test__one_plus_two(self):
        self.assertEqual(1 + 2, 3)

    def test__other_assertions(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)
        self.assertGreater(2, 1)
        self.assertLess(1, 2)
        self.assertIn(1, [1, 2])
        self.assertIsInstance(1, int)

    def test__exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
        with self.assertRaises(TypeError):
            1 + '2'

