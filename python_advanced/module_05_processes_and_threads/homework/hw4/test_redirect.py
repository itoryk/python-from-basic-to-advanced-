import unittest
from redirect import Redirect


class RedirectTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.stdout_text = 'stdout text'
        cls.stderr_text = 'stderr text'

    def test_stdout_stderr(self):

        with open('test_stdout.txt', 'w') as stdout_file, \
                open('test_stderr_txt', 'w') as stderr_file:
            with Redirect(stdout=stdout_file, stderr=stderr_file):
                print(self.stdout_text)
                raise Exception(self.stderr_text)
        with open('test_stdout.txt', 'r') as stdout_file, \
                open('test_stderr.txt', 'r') as stderr_file:
            stdout = stdout_file.read()
            stderr = stderr_file.read()

        self.assertTrue(self.stdout_text in stdout)
        self.assertTrue(self.stderr_text in stderr)

    def test_stdout_only(self):
        with open('test_stdout_only.txt', 'w') as stdout_file:
            with Redirect(stdout=stdout_file):
                print(self.stdout_text)

        with open('test_stdout_only.txt', 'r') as stdout_file:
            stdout = stdout_file.read()

        self.assertTrue(self.stdout_text in stdout)

    def test_stderr_only(self):
        with open('test_stderr_only.txt', 'w') as stderr_file:
            with Redirect(stderr=stderr_file):
                raise Exception(self.stderr_text)

        with open('test_stderr_only.txt', 'r') as stderr_file:
            stderr = stderr_file.read()

        self.assertTrue(self.stderr_text in stderr)

    def test_stdout_stderr_turn_off(self) -> None:
        with self.assertRaises(Exception):
            with open('stdout.txt', 'w') as file_out, \
                    open('stderr.txt', 'w') as file_err:
                with Redirect():
                    print(self.stdout_text)
                    raise Exception(self.stderr_text)

        with open('stdout.txt', 'r') as file_out, \
                open('stderr.txt', 'r') as file_err:
            stdout = file_out.read()
            stderr = file_err.read()

        self.assertFalse(self.stdout_text in stdout)
        self.assertFalse(self.stderr_text in stderr)


if __name__ == '__main__':
    unittest.main()
"""    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)"""
