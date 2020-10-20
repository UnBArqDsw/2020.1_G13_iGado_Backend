import json
import unittest

from project import db
from project.tests.base import BaseTestCase
from project.api.models.user import UserModel
from project.api.models.farm import FarmModel
from project.api.models.work import WorkModel


def add_user(fullname, email, password, is_proprietary):
    user = UserModel(fullname=fullname, email=email, password=password,
                     is_proprietary=is_proprietary)
    db.session.add(user)
    db.session.commit()
    return user


class TestUser(BaseTestCase):
    """Tests for the User."""

    def test_single_user(self):
        """Ensure get single User behaves correctly."""
        user = add_user(fullname='michael', email='michael@mherman.org',
                        password='123456', is_proprietary=True)
        farm = FarmModel("abc", 1000)
        db.session.add(farm)
        db.session.commit()
        work = WorkModel(1, 1)
        db.session.add(work)
        db.session.commit()
        with self.client:
            response = self.client.get(f'/user/{user.user_id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['data']['is_proprietary'], True)
            self.assertIn('michael', data['data']['fullname'])
            self.assertIn('michael@mherman.org', data['data']['email'])
            self.assertTrue(data['data']['password'])
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
            "is_proprietary": False,
        }
        user_one = UserModel(email=user_data['email'],
                             fullname=user_data['fullname'],
                             password=user_data['password'],
                             is_proprietary=user_data['is_proprietary'])
        user_two = UserModel(email=user_data['email'],
                             fullname=user_data['fullname'],
                             password=user_data['password'],
                             is_proprietary=user_data['is_proprietary'])
        self.assertNotEqual(user_one.password, user_two.password)

    def test_create_proprietary(self):
        with self.client:
            user_data = {
                "fullname": "João",
                "email": "test@test.com",
                "password": "123456",
                "is_proprietary": False,
                "farm_size": 100,
                "farm_name": "ABC"
            }
            response = self.client.post('/user/create',
                                        data=json.dumps(user_data),
                                        content_type='application/json',)
            self.assertEqual(201, response.status_code)

    def test_create_employee(self):
        with self.client:
            farm = FarmModel("abc", 1000)
            db.session.add(farm)
            db.session.commit()
            user_data = {
                "fullname": "João",
                "email": "test@test.com",
                "password": "123456",
                "is_proprietary": False,
                "farm_id": farm.farm_id,
                "farm_size": None,
                "farm_name": None
            }
            response = self.client.post('/user/create',
                                        data=json.dumps(user_data),
                                        content_type='application/json',)
            self.assertEqual(201, response.status_code)

    def test_create_user_missing_paramater(self):
        with self.client:
            user_data = {
                "fullname": "João",
                "email": "test@test.com",
                "is_proprietary": False,
            }
            response = self.client.post('/user/create',
                                        data=json.dumps(user_data),
                                        content_type='application/json',)
            self.assertEqual(400, response.status_code)

    def test_all_users(self):
        """Ensure get all users behaves correctly."""
        add_user(fullname='michael', email='michael@mherman.org',
                 password='123456', is_proprietary=True)
        add_user(fullname='fletcher', email='fletcher@notreal.com',
                 password='123123', is_proprietary=False)
        farm = FarmModel("abc", 1000)
        db.session.add(farm)
        db.session.commit()
        work = WorkModel(1, 1)
        db.session.add(work)
        db.session.commit()
        with self.client:
            response = self.client.get('/user')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertEqual(data['data']['users'][0]['is_proprietary'], True)
            self.assertIn('michael', data['data']['users'][0]['fullname'])
            self.assertIn(
                'michael@mherman.org', data['data']['users'][0]['email'])
            self.assertTrue(data['data']['users'][0]['password'])
            self.assertListEqual(
                [1], data['data']['users'][0]['farms'])
            self.assertEqual(data['data']['users'][1]['is_proprietary'], False)
            self.assertIn('fletcher', data['data']['users'][1]['fullname'])
            self.assertIn(
                'fletcher@notreal.com', data['data']['users'][1]['email'])
            self.assertTrue(data['data']['users'][0]['password'])
            self.assertListEqual(
                [], data['data']['users'][1]['farms'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
