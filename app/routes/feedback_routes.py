from flask import Blueprint, request, jsonify
from app.controllers.feedback_controller import FeedbackController

feedback_blueprint = Blueprint('feedback', __name__)
feedback_controller = FeedbackController()

@feedback_blueprint.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    feedback = feedback_controller.submit_feedback(data['user_id'], data['content'], data['created_at'])
    return jsonify({'user_id': feedback.user_id, 'content': feedback.content, 'created_at': feedback.created_at}), 201