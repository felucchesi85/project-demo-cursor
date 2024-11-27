from app.models.user import User

class UserController:
    def register_user(self, name: str, email: str) -> User:
        # Here you would add logic to save the user to a database
        return User(name, email)