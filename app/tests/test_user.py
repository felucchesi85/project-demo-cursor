import unittest
import logging
from app.models.user import User

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        logger.info("Testing user creation with valid data.")
        user = User(name="John Doe", email="john.doe@example.com")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john.doe@example.com")

    def test_user_email_format(self):
        logger.info("Testing user creation with invalid email format.")
        with self.assertRaises(ValueError):
            User(name="Jane Doe", email="invalid-email")

if __name__ == '__main__':
    unittest.main()