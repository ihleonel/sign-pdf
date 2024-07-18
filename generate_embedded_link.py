# -*- coding:utf-8 -*-
from decouple import config as env
from signnow_python_sdk import Config, OAuth2, Document

Config(client_id=env('CLIENT_ID'), client_secret=env('CLIENT_SECRET'), environment='production')

auth = OAuth2.request_token(env('USER_SIGNNOW'), env('PASS_SIGNNOW'))

# Get Document
document = Document.get(auth.get('access_token'), '8378b9db5d43457385ea4d6e8bd0eef6dc6c3959')

# Generate embedded link
payload = {
    "auth_method": "none",
    "link_expiration": 15
}
embedded_link = Document.embedded_invite_link(
    auth.get('access_token'),
    document.get('id'),
    '2f2d5de3809442fea5409b96589754111a539c2d',
    payload
)

print(embedded_link)
