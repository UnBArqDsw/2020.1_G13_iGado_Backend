import json
import unittest

from project import db
from project.tests.base import BaseTestCase
from project.api.models.user import UserModel
from project.api.models.farm import FarmModel
from project.api.models.work import WorkModel


def add_user(fullname, email, password, isProprietary, farms):
    user = UserModel(fullname=fullname, email=email, password=password,
                     isProprietary=isProprietary, farms=farms)
    db.session.add(user)
    db.session.commit()
    return user


class TestUser(BaseTestCase):
    """Tests for the User."""

    def test_single_user(self):
        """Ensure get single User behaves correctly."""
        user = UserModel(fullname='michael', email='michael@mherman.org',
                         password='123456', isproprietary=True)
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = self.client.get(f'/user/{user.user_id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['data']['is_proprietary'], True)
            self.assertIn('michael', data['data']['fullname'])
            self.assertIn('michael@mherman.org', data['data']['email'])
            self.assertIn('123456', data['data']['password'])
            self.assertListEqual([1], data['data']['farms'])
            self.assertIn('success', data['status'])

    def test_single_user_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('/user/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/user/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_password_are_random(self):
        user_data = {
            "fullname": "João",
            "email": "test@test.com",
            "password": "123456",
            "isproprietary": False,
        }
        user_one = UserModel(email=user_data['email'],
                             fullname=user_data['fullname'],
                             password=user_data['password'],
                             isproprietary=user_data['isproprietary'])
        user_two = UserModel(email=user_data['email'],
                             fullname=user_data['fullname'],
                             password=user_data['password'],
                             isproprietary=user_data['isproprietary'])
        self.assertNotEqual(user_one.password, user_two.password)

    def test_create_user(self):
        with self.client:
            user_data = {
                "fullname": "João",
                "email": "test@test.com",
                "password": "123456",
                "isproprietary": False,
            }
            response = self.client.post('/user/create',
                                        data=json.dumps(user_data),
                                        content_type='application/json')
            self.assertEqual(201, response.status_code)

    def test_create_user_missing_paramater(self):
        with self.client:
            user_data = {
                "fullname": "João",
                "email": "test@test.com",
                "isproprietary": False,
            }
            response = self.client.post('/user/create',
                                        data=json.dumps(user_data),
                                        content_type='application/json')
            self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    unittest.main()
