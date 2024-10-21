# -*- coding:utf-8 -*-
from decouple import config as env
from signnow_python_sdk import Document, Config, OAuth2

Config(
    client_id=env('CLIENT_ID'),
    client_secret=env('CLIENT_SECRET'),
    environment='production'
)

auth = OAuth2.request_token(env('USER_SIGNNOW'), env('PASS_SIGNNOW'))
Document.delete(auth.get('access_token'), '0dd64bce925444ae938a43e90070529dcbdb8b87')
