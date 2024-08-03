# -*- coding:utf-8 -*-
from decouple import config as env
from signnow_python_sdk import Config, OAuth2, Webhook

Config(
    client_id=env('CLIENT_ID'),
    client_secret=env('CLIENT_SECRET'),
    environment='production'
)

auth = OAuth2.request_token(env('USER_SIGNNOW'), env('PASS_SIGNNOW'))

payload = {
    'event': 'document.open',
    'entity_id': '76cc6005bbc741c38bd597056c7cefa021161f80',
    'action': 'callback',
    'atributes': {
        'callback': 'https://9530-38-51-88-192.ngrok-free.app/' # ngrok
    }
}

created = Webhook.create(auth.get('access_token'), payload)
print(created)

response = Webhook.list_all(auth.get('access_token'))
print(response)
