from app.models.feedback import Feedback

class FeedbackController:
    def submit_feedback(self, user_id: int, content: str, created_at: str) -> Feedback:
        # Here you would add logic to save the feedback to a database
        return Feedback(user_id, content, created_at)