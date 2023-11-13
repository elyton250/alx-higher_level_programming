import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        """Set up common objects for testing."""
        self.square1 = Square(5, 2, 3, 1)
        self.square2 = Square(3, id=2)

    def test_attributes(self):
        """Test the attributes of the Square."""
        self.assertEqual(self.square1.id, 1)
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square1.x, 2)
        self.assertEqual(self.square1.y, 3)

        self.assertEqual(self.square2.id, 2)
        self.assertEqual(self.square2.size, 3)
        self.assertEqual(self.square2.x, 0)
        self.assertEqual(self.square2.y, 0)

    def test_str_representation(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.square1), "[Square] (1) 2/3 - 5")
        self.assertEqual(str(self.square2), "[Square] (2) 0/0 - 3")

    def test_size_setter(self):
        """Test the size setter method."""
        self.square1.size = 10
        self.assertEqual(self.square1.size, 10)
        self.assertEqual(self.square1.width, 10)
        self.assertEqual(self.square1.height, 10)

    def test_update_method(self):
        """Test the update method."""
        self.square2.update(5, 2, 1, 0)
        self.assertEqual(self.square2.id, 5)
        self.assertEqual(self.square2.size, 2)
        self.assertEqual(self.square2.x, 1)
        self.assertEqual(self.square2.y, 0)

    def test_to_dictionary_method(self):
        """Test the to_dictionary method."""
        dictionary1 = self.square1.to_dictionary()
        self.assertEqual(dictionary1, {'id': 1, 'size': 5, 'x': 2, 'y': 3})

        dictionary2 = self.square2.to_dictionary()
        self.assertEqual(dictionary2, {'id': 2, 'size': 3, 'x': 0, 'y': 0})

    def test_area_method(self):
        """Test the area method."""
        self.assertEqual(self.square1.area(), 25)
        self.assertEqual(self.square2.area(), 9)
        
if __name__ == '__main__':
    unittest.main()
