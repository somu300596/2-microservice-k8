# order-service/app.py
import requests
from flask import Flask, jsonify

app = Flask(__name__)

USER_SERVICE_URL = "http://user-service/users"

@app.route('/orders/<int:user_id>', methods=['GET'])
def get_orders(user_id):
    orders = {
        1: [{"id": 101, "product": "Laptop", "amount": 999.99}],
        2: [{"id": 102, "product": "Smartphone", "amount": 499.99}]
    }
    
    # Call the User Service to get user information
    user_response = requests.get(f"{USER_SERVICE_URL}/{user_id}")
    if user_response.status_code == 200:
        user_info = user_response.json()
        return jsonify({
            "user": user_info,
            "orders": orders.get(user_id, "No orders found")
        }), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
