import json
import unittest

from project import db
from project.tests.base import BaseTestCase
from project.api.models.proprietary import ProprietaryModel

class TestProprietary(BaseTestCase):
    """Tests for the Proprietary."""

    def test_single_proprietary(self):
        """Ensure get single proprietary behaves correctly."""
        proprietary = ProprietaryModel(fullname='michael', email='michael@mherman.org', password='123456')
        db.session.add(proprietary)
        db.session.commit()
        with self.client:
            response = self.client.get(f'/proprietaries/{proprietary.idProprietary}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('michael', data['data']['fullname'])
            self.assertIn('michael@mherman.org', data['data']['email'])
            self.assertIn('123456', data['data']['password'])
            self.assertIn('success', data['status'])

if __name__ == '__main__':
    unittest.main()