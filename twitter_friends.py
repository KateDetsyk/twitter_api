import base64
import requests
import json


auth_url = "https://api.twitter.com/oauth2/token"
key_string = base64.b64encode(b"opzngiTQvFF80YtlP36KStsRw:3lPmht0Gq8cpfUOWI5ePppSGis687lu3lTIjwTm2gRpcKLo0OK").decode('utf-8')


def fetch_auth_token():
    resp = requests.post(
        auth_url,
        headers={
            "Authorization": "Basic {k}".format(k=key_string),
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
        data={"grant_type": "client_credentials"})
    return resp.json()['access_token']


access_token = fetch_auth_token()


result = []
cursor = -1
while cursor:
    resp = requests.get(auth_url.format(c=str(cursor)), headers={'Authorization': 'Bearer {ak}'.format(ak=access_token)})
    data = resp.json()
    result.extend(data['users'])
    cursor = data['next_cursor']
