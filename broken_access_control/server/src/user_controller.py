import os
import json
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERDATA_DIR = os.path.join(BASE_DIR, '../data/users.json')


def get_user_data(user):
    '''
    Retrive data for user from users.json
    '''
    try:
        with open(USERDATA_DIR, 'r') as f:
            users = json.load(f)
            return users.get(user)
    except Exception as e:
        return None

def is_admin(authToken):
    '''
    Determine if this user is able to access the admin panel.
    '''
    try:
        data = load_token(authToken)
        role = data.get('role')
        return role == 'admin'
    
    except Exception as e:
        print(f'is_admin: Error: {e}')
    
def create_token(user_data):
    '''
    Create a token for the session.
    The token contains user preferences and roles.

    We are now encoding just a JSON object.
    '''
    try:
        # convert the user_data into a http friend string
        authToken = base64.b64encode(json.dumps(user_data).encode()).decode('utf-8')
        return authToken
    except Exception as e:
        return None
    
def load_token(authToken): 
    '''
    Decode and load token

    No pickles to be found. Just JSON
    '''
    user_data = json.loads(base64.b64decode(authToken).decode())

    return user_data
    