class User:
    def __init__(self, name, email):
        self.name = name
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")
        self.email = email

    def _is_valid_email(self, email):
        # Simple check for email format
        return "@" in email and "." in email