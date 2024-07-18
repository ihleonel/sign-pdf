# -*- coding:utf-8 -*-
from decouple import config
import requests

class Token:
    def __init__(self) -> None:
        self.base_url = 'https://api.signnow.com'
        self.token_url = f'{self.base_url}/oauth2/token'
        self.token_basic = config('TOKEN_BASIC')

        self.username = config('USER_SIGNNOW')
        self.password = config('PASS_SIGNNOW')

    def access_token(self) -> str:
        headers = {
            'Authorization': f'Basic {self.token_basic}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        auth_data = {
            'username': self.username,
            'password': self.password,
            'grant_type': 'password',
            'scope': '*',
        }

        response = requests.post(self.token_url, data=auth_data, headers=headers)
        access_token = response.json()

        return access_token.get('access_token')
