# -*- coding:utf-8 -*-
import requests
from datetime import datetime
from services.sign_now.token import Token

token = Token()
access_token = token.access_token()

UPLOAD_URL = 'https://api.signnow.com/document/fieldextract'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/json',
}

file_path = './documents/test-sign-document-2.pdf'
now = datetime.now()

with open(file_path, 'rb') as file:
    files = {'file': (file.name, file, 'application/pdf')}
    response = requests.post(UPLOAD_URL, headers=headers, files=files)

json = response.json()

print(json)
