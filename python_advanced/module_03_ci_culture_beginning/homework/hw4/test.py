import unittest
from person import Person


class TestPerson(unittest.TestCase):

    def test_name(self):
        data = Person('Vasya', 1972, 'Gercena-37')
        self.assertEqual(data.get_name(), 'Vasya')

    def test_age(self):
        data = Person('Vasya', 1972, 'Gercena-37')
        self.assertEqual(data.get_age(), 52)

    def test_street(self):
        data = Person('Vasya', 1972, 'Gercena-37')
        self.assertEqual(data.get_address(), 'Gercena-37')

    def test_is_homeless(self):
        data = Person('Vasya', 1972, None)
        self.assertTrue(data.is_homeless(), None)
