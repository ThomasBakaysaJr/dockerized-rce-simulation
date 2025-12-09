import os
import json
import base64
import hmac
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERDATA_DIR = os.path.join(BASE_DIR, '../data/users.json')

HMAC_KEY = b'SUPER-SECRET-KEY'

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

def create_token(data):
    '''
    Create a auth token of data with an hmac signature attached
    '''
    encoded_json = encode_json(data)
    signature = create_hmac(data).hexdigest()
    return f'{encoded_json}.{signature}'

def is_admin(auth_token):
    '''
    Determine if this user is able to access the admin panel.
    '''
    try:
        data = decode_json(auth_token)
        role = data.get('role')
        return role == 'admin'
    
    except Exception as e:
        print(f'is_admin: Error: {e}')
    
def encode_json(user_data):
    '''
    Encode user_data into a http friendly string

    This uses python pickle - which is very unsecure.
    '''
    try:
        # convert the user_data into a http friend string
        encoded_json = base64.b64encode(json.dumps(user_data).encode()).decode('utf-8')
        return encoded_json
    except Exception as e:
        return None
    
def decode_json(user_data): 
    '''
    Decode and load token

    Uses python pickle - INSECURE
    '''
    user_data = json.loads(base64.b64decode(user_data).decode())

    return user_data

# def encode_digest(digest):
#     return digest.decode('utf-8')

# def decode_digest(digest):
#     return base64.b64encode(digest)

def check_signature(auth_token):
    # seperated the encoded json and the signature
    in_encoded_json, signature = auth_token.split('.')

    in_data = decode_json(in_encoded_json)

    # Difference
    # Here we make sure that that the data hasn't been tampered with
    return compare_hmac(in_data, signature)

def create_hmac(user_data) -> hmac:
    '''
    Create and return a hmac signature for the byte
    :param user_data: JSON object
    '''
    auth_token_bytes = json.dumps(user_data).encode('utf-8')
    hmac_obj = hmac.new(HMAC_KEY, auth_token_bytes, hashlib.sha256)
    return hmac_obj

def compare_hmac(in_encoded_data, in_signature):
    '''
    Crate an hmac for this incoming token and compare it
    to the received hmac.
    
    :param auth_token: JSON Object - untrusted auth token
    :param incoming_hmac: Received HMAC hex signature - trusted

    :return If the two signatures match
    '''
    user_data = decode_json(in_encoded_data)
    new_signature = create_hmac(user_data).hexdigest()
    return hmac.compare_digest(new_signature, in_signature)
