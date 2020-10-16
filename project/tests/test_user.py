import json
import unittest

from project import db
from project.tests.base import BaseTestCase
from project.api.models.user import UserModel

class TestUser(BaseTestCase):
    """Tests for the User."""

    def test_single_user(self):
        """Ensure get single User behaves correctly."""
        user = UserModel(fullname='michael', email='michael@mherman.org', password='123456', isProprietary=True)
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = self.client.get(f'/users/{user.idUser}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['data']['isProprietary'], True)
            self.assertIn('michael', data['data']['fullname'])
            self.assertIn('michael@mherman.org', data['data']['email'])
            self.assertIn('123456', data['data']['password'])
            self.assertIn('success', data['status'])

if __name__ == '__main__':
    unittest.main()