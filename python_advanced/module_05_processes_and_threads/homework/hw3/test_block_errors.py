import unittest
from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_ZeroDivisionError(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors({TypeError}):
                a = 1/0
            print('Success')

    def test_TypeError(self) -> None:
        with self.assertRaises(TypeError):
            with BlockErrors({ZeroDivisionError}):
                a = 1/'0'
            print('Success')

    def test_TypeError2(self) -> None:
        with self.assertRaises(TypeError):
            with BlockErrors({}):
                with BlockErrors({ZeroDivisionError}):
                    a = 1/'0'
                print('Indoor unit: Success')
            print('External unit: Success')

    def test_Exception(self) -> None:
        with self.assertRaises(Exception):
            with BlockErrors({}):
                a = 1/'0'
            print('Success')


if __name__ == '__main__':
    unittest.main()
