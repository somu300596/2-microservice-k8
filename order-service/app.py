# order-service/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders/<int:user_id>', methods=['GET'])
def get_orders(user_id):
    orders = {
        1: [{"id": 101, "product": "Laptop", "amount": 999.99}],
        2: [{"id": 102, "product": "Smartphone", "amount": 499.99}]
    }
    return jsonify(orders.get(user_id, "No orders found")), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
