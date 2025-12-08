from flask import Flask

app = Flask(__name__)

@app.route("/login")
def get_auth_token():
    authToken = make_auth_token()
    return authToken

# helper functions
def make_auth_token():
