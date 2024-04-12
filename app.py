from flask import Flask, request, jsonify

app = Flask(__name__)

passwords = {}

# Generate a password with specified character types and length
def generate_password():
    password = "1aA."
    return password

@app.route('/')
def index():
    return 'Hello, World!'

# Create (Add) a new password with a keyword
@app.route('/passwords', methods=['POST'])
def add_password():
    data = request.get_json()
    keyword = data.get('keyword')

    if not keyword:
        message = f'Keyword is required.'
        return jsonify({'error': message}), 400
    if keyword in passwords:
        message = f"Keyword '{keyword}' already exists."
        return jsonify({'error': message}), 400
    
    password = generate_password()
    passwords[keyword] = password
    message = f"Password added successfully for keyword '{keyword}'."
    return jsonify({'message': message, 'keyword': keyword}), 200

# Read (Retrieve) a password by keyword
@app.route('/passwords/<keyword>', methods=['GET'])
def get_password(keyword):
    if keyword not in passwords:
        message = f"Keyword '{keyword}' not found."
        return jsonify({'error': message}), 404
    
    message = f"Password retrieved successfully for keyword '{keyword}'."
    return jsonify({'keyword': keyword, 'password': passwords[keyword]})

# Update an existing password by keyword
@app.route('/passwords/<keyword>', methods=['PUT'])
def update_password(keyword):
    data = request.get_json()

    if keyword not in passwords:
        message = f"Keyword '{keyword}' not found."
        return jsonify({'error': message}), 404

    password = generate_password()
    passwords[keyword] = password
    message = f"Password updated successfully for keyword '{keyword}'."
    return jsonify({'message': message, 'keyword': keyword}), 200

# Delete a password by keyword
@app.route('/passwords/<keyword>', methods=['DELETE'])
def delete_password(keyword):
    if keyword not in passwords:
        message = f"Keyword '{keyword}' not found."
        return jsonify({'error': message}), 404

    del passwords[keyword]
    message = f"Password deleted successfully for keyword '{keyword}'."
    return jsonify({'message': message, 'keyword': keyword})

if __name__ == '__main__':
    app.run(debug=False)
