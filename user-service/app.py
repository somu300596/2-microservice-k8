# user-service/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {
        1: {"name": "John Doe", "email": "john@example.com"},
        2: {"name": "Jane Smith", "email": "jane@example.com"}
    }
    return jsonify(users.get(user_id, "User not found")), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
