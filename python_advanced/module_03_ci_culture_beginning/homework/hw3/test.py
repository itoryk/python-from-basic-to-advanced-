import unittest
from accounting import app
import accounting


class TestEndPoints(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = app.test_client()
        accounting.storage = {
            2024: {
                1: {
                    1: 100,
                    2: 150},
                2: {1: 100,
                    2: 150},
                3: {1: 100,
                    2: 150},
                4: {1: 100,
                    2: 150}
            }
        }

    def test_add_valid_date(self):
        response = self.app.get('/add/20240404/250')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(accounting.storage[2024][4][4], 250)

    def test_calculate_year(self):
        response = self.app.get('/calculate/2024')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 1000)

    def test_calculate_date(self):
        response = self.app.get('/calculate/2024/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 250)




