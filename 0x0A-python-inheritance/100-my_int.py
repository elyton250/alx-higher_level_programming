#!/usr/bin/python3
"""this modeule adds atributes"""
class MyInt(int):
    """
    MyInt class that inherits from int with inverted == and != operators.
    """

    """def __init__(self, value):
        
        Initialize MyInt with a given value.
        Args:
            value (int): The integer value.
        super().__init__(value)"""

    def __eq__(self, other):
        """
        Check if two MyInt objects are not equal.
        Args:
            other (MyInt or int): The other MyInt or integer to compare.
        Returns:
            bool: True if they are not equal, False otherwise.
        """
        return super().__eq__(other)

    def __ne__(self, other):
        """
        Check if two MyInt objects are equal.
        Args:
            other (MyInt or int): The other MyInt or integer to compare.
        Returns:
            bool: True if they are equal, False otherwise.
        """
        return not super().__eq__(other)
