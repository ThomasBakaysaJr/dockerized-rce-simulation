from flask import Flask, request, jsonify
from flask_cors import CORS

import src.user_controller as usr_ctrl

app = Flask(__name__)
# Get around CORS & preflight checks
CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "allow_headers": ["Authorization", "Content-Type"]}})

USERS_FILE = 'data/users.json'

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    if data is None:
        print(f'warning: {data}.get_json() is returning None')
        return jsonify({'error' : f'Invalid Request'}), 400
    
    user_id = data.get('user_id')

    user_data = usr_ctrl.get_user_data(user_id)
    if user_data is None:
        print(f'warning: {user_id} is not a valid user_id')
        return jsonify({'error' : f'Invalid Login'}), 400
    
    authToken = usr_ctrl.create_token(user_data)
    
    return_data = {
        'user_data': user_data,
        'authToken': authToken
    }

    return jsonify(return_data)

@app.route("/access_admin", methods=['GET'])
def access_admin():
    auth_header = request.headers
    if auth_header is None:
        print(f'warning: No authorization header available')
        return jsonify({'error' : f'Missing Headers'}), 400
    
    encoded_token = auth_header.get('Authorization').split(" ")[1]

    return_data = {
        'is_elevated' : usr_ctrl.is_admin(encoded_token)
    }

    return return_data


if __name__ == "__main__":
    '''
    Bind the flask app to localhost:5000
    '''
    print(f'[SERVER] Starting Flask App')
    app.run(host='0.0.0.0', port=5000, debug=True)
