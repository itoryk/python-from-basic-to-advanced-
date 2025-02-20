import unittest
from remote_execution import app


class RemoteExecutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        cls.app = app.test_client()
        cls.base_url = "/run_code"

    def setUp(self) -> None:
        self.data = {'code': 'print("Hello world")', 'timeout': 1}

    def test_timeout(self):
        result = self.app.post(self.base_url, data=self.data)
        self.assertNotEqual(result.data.decode(), "time's up")

    def test_form_valid(self):
        result = self.app.post(self.base_url, data=self.data)
        self.assertNotIn('invalid input', result.data.decode())

    def test_shell(self):
        result = self.app.post(self.base_url, data=self.data)
        self.assertNotEqual(result.data.decode(), "field CODE cannot contain the string 'shell=True'")


if __name__ == '__main__':
    unittest.main()
