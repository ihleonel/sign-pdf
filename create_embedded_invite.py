# -*- coding:utf-8 -*-
from decouple import config as env
from signnow_python_sdk import Config, OAuth2, Document

Config(client_id=env('CLIENT_ID'), client_secret=env('CLIENT_SECRET'), environment='production')

auth = OAuth2.request_token(env('USER_SIGNNOW'), env('PASS_SIGNNOW'))

# Get Document
document = Document.get(auth.get('access_token'), '8378b9db5d43457385ea4d6e8bd0eef6dc6c3959')

print(document.get('fields'))

# Create embedded invite
invite_payload = {
    'invites': [
        {
            'email': 'ibarra.h.leonel@gmail.com',
            'role': 'worker',
            'order': 1,
            'auth_method': 'none',
            'first_name': 'first name',
            'last_name': 'last name',
        },
        {
            'email': 'leo_metalero22@hotmail.com',
            'role': 'employer',
            'order': 2,
            'auth_method': 'none',
            'first_name': 'first meta',
            'last_name': 'last meta',
        },
    ]
}

embedded = Document.embedded_invite(auth.get('access_token'), document.get('id'), invite_payload)

print(embedded)
