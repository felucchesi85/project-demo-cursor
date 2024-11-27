class Feedback:
    def __init__(self, user_id: int, content: str, created_at: str):
        if not content:
            raise ValueError("Content cannot be empty")
        self.user_id = user_id
        self.content = content
        self.created_at = created_at