#!/usr/bin/python3
"""This module test max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxTest(unittest.TestCase):
    """This class is for testing"""

    def test_empty_list(self):
        """Test empty list"""
        m_list = []
        result = max_integer(m_list)
        self.assertEqual(result, None)

    def test_undodered(self):
        """Tests in unorderred"""
        m_list = [10, 2, 8, 11]
        result = max_integer(m_list)
        self.assertEqual(result, 11)

    def test_odered(self):
        """Tests in orderred"""
        m_list = [1, 2, 3, 11]
        result = max_integer(m_list)
        self.assertEqual(result, 11)
    def test_ele(self):
        """Tests one element"""
        m_list = [10]
        result = max_integer(m_list)
        self.assertEqual(result, 10)

    def test_floats(self):
        """Test floats if they work"""
        m_list = [2.0, 1.0, 3.0]
        result = max_integer(m_list)
        self.assertEqual(result, 3.0)

    def test_floats_int(self):
        """Test floats and intsif they work"""
        m_list = [2.0, 1, 3.0]
        result = max_integer(m_list)
        self.assertEqual(result, 3.0)

    def test_string(self):
        """Test strings if they work"""
        m_list = "bre"
        result = max_integer(m_list)
        self.assertEqual(result, 'r')

    def test_empt_strings(self):
        """Test strings if they work"""
        m_list = ""
        result = max_integer(m_list)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
