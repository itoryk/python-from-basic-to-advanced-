"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app


class TestForms(unittest.TestCase):

    def test(self):
        self.app = app.test_client()
        response = self.app.post(
            '/registration', data={
                'email': 'qwerty123@mail.com',
                'phone': '1234567890',
                'name': 'Pepe',
                'address': 'asdf12',
                'index': '112233'
            }
        )
        return response.status_code == 200

    def test_invalid_email(self):
        self.app = app.test_client()
        response = self.app.post(
            '/registration', data={
                'email': 'qwerty123mail.com',
                'phone': '1234567890',
                'name': 'Pepe',
                'address': 'asdf12',
                'index': '112233'
            }
        )
        return response.status_code == 400

    def test_invalid_phone(self):
        self.app = app.test_client()
        response = self.app.post(
            '/registration', data={
                'email': 'qwerty123@mail.com',
                'phone': '123456789011',
                'name': 'Pepe',
                'address': 'asdf12',
                'index': '112233'
            }
        )
        return response.status_code == 400

    def test_invalid_name(self):
        self.app = app.test_client()
        response = self.app.post(
            '/registration', data={
                'email': 'qwerty123@mail.com',
                'phone': '1234567890',
                'name': ' ',
                'address': 'asdf12',
                'index': '112233'
            }
        )
        return response.status_code == 400

    def test_invalid_address(self):
        self.app = app.test_client()
        response = self.app.post(
            '/registration', data={
                'email': 'qwerty123@mail.com',
                'phone': '1234567890',
                'name': 'Pepe',
                'address': ' ',
                'index': '112233'
            }
        )
        return response.status_code == 400

    def test_invalid_index(self):
        self.app = app.test_client()
        response = self.app.post(
            '/registration', data={
                'email': 'qwerty123@mail.com',
                'phone': '1234567890',
                'name': 'Pepe',
                'address': 'asdf12',
                'index': '11223311'
            }
        )
        return response.status_code == 400


if __name__ == '__main__':
    unittest.main()







"""
def test_email_validation():
    form = RegistrationForm(email='qwerty123@mail.com')
    assert form.email.validators(form)

    form = RegistrationForm(email='qwerty123mail.com')
    assert not form.email.validators(form)


def test_phone_validation():
    form = RegistrationForm(phone='1234567890')
    assert form.phone.validators(form)

    form = RegistrationForm(phone='12345678901')
    assert not form.phone.validators(form)


def test_name_validation():
    form = RegistrationForm(name='Pepe')
    assert form.name.validators(form)

    form = RegistrationForm(name=12345)
    assert not form.name.validators(form)


def test_address_validation():
    form = RegistrationForm(address='asdf,12')
    assert form.address.validators(form)

    form = RegistrationForm(address=12334)
    assert not form.address.validators(form)


def test_index_validation():
    form = RegistrationForm(index='112233')
    assert form.index.validators(form)

    form = RegistrationForm(index='11223344')
    assert not form.index.validators(form)
    
"""







