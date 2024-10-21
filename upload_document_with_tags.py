# -*- coding:utf-8 -*-
from decouple import config as env
from signnow_python_sdk import Config, OAuth2, Document

Config(
    client_id=env('CLIENT_ID'),
    client_secret=env('CLIENT_SECRET'),
    environment='production'
)

auth = OAuth2.request_token(env('USER_SIGNNOW'), env('PASS_SIGNNOW'))

# Upload document with tag sign
file_path = './documents/test-sign-document-3.pdf'
document = Document.upload(auth.get('access_token'), file_path, True)

# download = Document.download(
#     auth.get('access_token'),
#     document.get('id'),
#     "name_of_documento_downloaded",
#     "/home/leonel/github/sign-pdf/"
# )
