# -*- coding:utf-8 -*-
from decouple import config as env
from signnow_python_sdk import Config, OAuth2, Document

Config(client_id=env('CLIENT_ID'), client_secret=env('CLIENT_SECRET'), environment='production')

auth = OAuth2.request_token(env('USER_SIGNNOW'), env('PASS_SIGNNOW'))

# Upload document with tag sign
file_path = './documents/test-sign-document-2.pdf'
document = Document.upload(auth.get('access_token'), file_path, True)

# Send invite to sign document
invite_payload = {
    'from': 'leonel.ibarra@outsourcearg.com',
    'to': [
        {
            'email': 'ibarra.h.leonel@gmail.com',
            'role_id': '',
            'role': 'worker',
            'order': 1,
        },
        {
            'email': 'leonel.ibarra@outsourcearg.com',
            'role_id': '',
            'role': 'employer',
            'order': 2,
        }
    ]
}

response = Document.invite(auth.get('access_token'), document.get('id'), invite_payload)

print(response)
