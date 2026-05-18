import unittest
from rectangle import area, perimeter

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEquals(area(4, 5), 20, 'message')

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, '5')

    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)

class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        self.assertEquals(perimeter(4, 5), 18, 'message')

    def test_perimeter_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, perimeter, '4', 5)
        self.assertRaises(TypeError, perimeter, 4, '5')

    def test_perimeter_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, perimeter, -4, 5)
        self.assertRaises(ValueError, perimeter, 4, -5)

if __name__ == '__main__':
    unittest.main(verbosity=2)