from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user})
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    name = data.get('name')
    users[user_id] = name
    return jsonify({"message": "User added"}), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    if user_id in users:
        users[user_id] = name
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
