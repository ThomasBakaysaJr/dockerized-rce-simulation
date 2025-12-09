import os
import json
import pickle
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