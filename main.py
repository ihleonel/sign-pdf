# -*- coding:utf-8 -*-
from decouple import config
import requests

BASE_URL = 'https://api.signnow.com'
TOKEN_URL = f'{BASE_URL}/oauth2/token'
TOKEN_BASIC = config('TOKEN_BASIC')

username = config('USER_SIGNNOW')
password = config('PASS_SIGNNOW')

headers = {
    'Authorization': f'Basic {TOKEN_BASIC}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

auth_data = {
    'username': username,
    'password': password,
    'grant_type': 'password',
    'scope': '*',
}

response = requests.post(TOKEN_URL, data=auth_data, headers=headers)
access_token = response.json()

print(access_token)
