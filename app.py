from flask import Flask, request, jsonify
from password_generator import random_password
from password_encrypt import generateKey, encryptPassword, decryptPassword, encryptMasterPassword, verifyMasterPassword
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)


# users = {username: {hashedPassword, key, passwords={}}}
users = {}
passwords = {}

""" 
Add a User login to get a key meanwhile the key is random
"""
key = generateKey()


@app.route('/')
def index():
    return 'Hello, World!'

@app.errorhandler(500)
def server_error(error):
    logging.exception('An exception occurred during a request.')
    return 'Internal Server Error', 500

# Create a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not (username and password):
        message = f'Username and password fields are required'
        logging.error(message)
        return jsonify({'error': message}), 400
    
    if username in users:
        message = f"Username '{username}' already exists."
        logging.error(message)
        return jsonify({'error': message}), 400
    
    key = generateKey()
    hashedPassword = encryptMasterPassword(password)
    users[username] = {'hashedPassword': hashedPassword, 'key': key, 'passwords': {}}
    message = f"User '{username}' signed succesfully."
    logging.info(message)
    return jsonify({'message': message, 'username': username}), 200

@app.route('users/<username>', methods=['GET'])
def get_passwords(username):
    password = request.args.get('password')
    if not username in users:
        message = f'Username doesn\'t exist'
        logging.error(message)
        return jsonify({'error': message}), 400
    if not (verifyMasterPassword(password, users[username]['hasedPassword'])):
        message = f'Password incorrect'
        logging.error(message)
        return jsonify({'error': message}), 400

    global passwords
    passwords = users[username]['passwords']
    message = f"User '{username} signed succesfully'."
    logging.info(message)
    return jsonify({'message': message, 'username': username}), 200

# Create (Add) a new password with a keyword
@app.route('/passwords', methods=['POST'])
def add_password():
    data = request.get_json()
    keyword = data.get('keyword')
    length = data.get('length')
    lowercase = data.get('lowercase')
    uppercase = data.get('uppercase')
    digits = data.get('digits')
    punctuation = data.get('punctuation')

    if not (keyword and length and lowercase and uppercase and digits and punctuation) :
        message = f'Keyword, length, lowercase, uppercase, digits, and punctuation fields are required.'
        logging.error(message)
        return jsonify({'error': message}), 400
    if keyword in passwords:
        message = f"Keyword '{keyword}' already exists."
        logging.error(message)
        return jsonify({'error': message}), 400
    
    password = random_password(length, lowercase, uppercase, digits, punctuation)
    passwords[keyword] = encryptPassword(key,password)
    message = f"Password added successfully for keyword '{keyword}'."
    logging.info(message)
    return jsonify({'message': message, 'keyword': keyword}), 200

# Read (Retrieve) a password by keyword
@app.route('/passwords/<keyword>', methods=['GET'])
def get_password(keyword):
    if keyword not in passwords:
        message = f"Keyword '{keyword}' not found."
        logging.error(message)
        return jsonify({'error': message}), 404
    
    message = f"Password retrieved successfully for keyword '{keyword}'."
    logging.info(message)
    return jsonify({'keyword': keyword, 'password': decryptPassword(key, passwords[keyword])})

# Update an existing password by keyword
@app.route('/passwords/<keyword>', methods=['PUT'])
def update_password(keyword):
    data = request.get_json()
    length = data.get('length')
    lowercase = data.get('lowercase')
    uppercase = data.get('uppercase')
    digits = data.get('digits')
    punctuation = data.get('punctuation')

    if not (keyword and length and lowercase and uppercase and digits and punctuation) :
        message = f'Keyword, length, lowercase, uppercase, digits, and punctuation fields are required.'
        logging.error(message)
        return jsonify({'error': message}), 400
    if keyword not in passwords:
        message = f"Keyword '{keyword}' not found."
        logging.error(message)
        return jsonify({'error': message}), 404

    password = random_password(length, lowercase, uppercase, digits, punctuation)
    passwords[keyword] = encryptPassword(key, password)
    message = f"Password updated successfully for keyword '{keyword}'."
    logging.info(message)
    return jsonify({'message': message, 'keyword': keyword}), 200

# Delete a password by keyword
@app.route('/passwords/<keyword>', methods=['DELETE'])
def delete_password(keyword):
    if keyword not in passwords:
        message = f"Keyword '{keyword}' not found."
        logging.error(message)
        return jsonify({'error': message}), 404

    del passwords[keyword]
    message = f"Password deleted successfully for keyword '{keyword}'."
    logging.info(message)
    return jsonify({'message': message, 'keyword': keyword})

if __name__ == '__main__':
    app.run(debug=False)
