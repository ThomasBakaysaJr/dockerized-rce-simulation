import json
import pickle
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USERS_FILE = 'data/users.json'

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json
    user_id = data.get('user_id')

    user_data = get_user_data(user_id)
    if user_data is None:
        return jsonify({'error' : 'Invalid JSON'}), 400
    
    token = create_token(user_data)

    json_token = {
        'status' : 'success',
        'user_pref' : user_data,
        'token' : token
    }

    return jsonify(json_token)
    

# helper functions
def get_user_data(user):
    '''
    Retrive data for user from users.json
    '''
    try:
        with open(USERS_FILE, 'r') as f:
            users = json.load(f)
            return users.get('user')
    except Exception as e:
        return None
    
def create_token(user_data):
    '''
    Create a token for the session
    This uses python pickle - which is very unsecure
    '''
    try:
        pickled_data = pickle.dumps(user_data)
        token = base64.b64encode(pickled_data).decode('utf-8')
        return token
    except Exception as e:
        return None
    
if __name__ == "__main__":
    '''
    Bind the flask app to localhost:5000
    '''
    print(f'[SERVER] Starting Flask App')
    app.run(host='0.0.0.0', port=5000, debug=True)
