from flask import Flask
from app.routes.user_routes import user_blueprint
from app.routes.feedback_routes import feedback_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(feedback_blueprint)

if __name__ == '__main__':
    app.run(debug=True)