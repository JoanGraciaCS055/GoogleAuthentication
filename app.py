from flask import Flask, redirect, request, render_template
import requests

app = Flask(__name__)

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'https://flask-app-5lgdh7t6mq-ey.a.run.app/oauth2callback'

@app.route('/login')
def login():
    authorization_url = (
        "https://accounts.google.com/o/oauth2/auth?"
        "client_id={}&"
        "redirect_uri={}&"
        "response_type=code&"
        "scope=https://www.googleapis.com/auth/userinfo.email"
    ).format(CLIENT_ID, REDIRECT_URI)
    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    code = request.args.get('code')
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    response = requests.post(token_url, data=data)
    tokens = response.json()
    access_token = tokens.get('access_token')

    if not access_token:
        return render_template('error.html', message='Failed to obtain access token')
    else:
        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        headers = {'Authorization': f'Bearer {access_token}'}
        userInformation = requests.get(userinfo_url, headers=headers).json()
        email = userInformation.get('email')

        return render_template('token.html', token=access_token)
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
