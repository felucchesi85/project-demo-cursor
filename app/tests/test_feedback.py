import unittest
import logging
from app.models.feedback import Feedback

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestFeedback(unittest.TestCase):
    def test_feedback_creation(self):
        logger.info("Testing feedback creation with valid data.")
        feedback = Feedback(user_id=1, content="Great service!", created_at="2023-10-01T12:00:00Z")
        self.assertEqual(feedback.user_id, 1)
        self.assertEqual(feedback.content, "Great service!")
        self.assertEqual(feedback.created_at, "2023-10-01T12:00:00Z")

    def test_feedback_content_length(self):
        logger.info("Testing feedback creation with empty content.")
        with self.assertRaises(ValueError):
            Feedback(user_id=1, content="", created_at="2023-10-01T12:00:00Z")

if __name__ == '__main__':
    unittest.main()