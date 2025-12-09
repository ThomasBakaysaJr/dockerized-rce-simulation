from flask import Flask, request, jsonify
from flask_cors import CORS

import src.user_controller as usr_ctrl

app = Flask(__name__)
CORS(app)

USERS_FILE = 'data/users.json'

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('user_id')

    user_data = usr_ctrl.get_user_data(user_id)
    if user_data is None:
        print(f'warning: {user_id} is not a valid user_id')
        return jsonify({'error' : f'Invalid Login'}), 400
    
    token = usr_ctrl.create_token(user_data)

    json_token = {
        'status' : 'success',
        'user_pref' : user_data,
        'token' : token
    }

    return jsonify(json_token)
    
if __name__ == "__main__":
    '''
    Bind the flask app to localhost:5000
    '''
    print(f'[SERVER] Starting Flask App')
    app.run(host='0.0.0.0', port=5000, debug=True)
