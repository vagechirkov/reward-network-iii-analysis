import os
from datetime import datetime

import requests
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    # read constants from environment variables
    BACKEND_USER = os.environ['BACKEND_USER']
    BACKEND_PASSWORD = os.environ['BACKEND_PASSWORD']
    BACKEND_URL = os.environ['BACKEND_URL']
    url = f'https://{BACKEND_URL}/results'
    headers = {'Accept': 'application/json'}
    auth = (BACKEND_USER, BACKEND_PASSWORD)
    subjects = requests.get(f'{url}/subjects', headers=headers, auth=auth)
    current_datatime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    with open(f'subjects_{current_datatime}.json', 'wb') as out_file:
        out_file.write(subjects.content)

    sessions = requests.get(f'{url}/sessions', headers=headers, auth=auth)
    with open(f'sessions_{current_datatime}.json', 'wb') as out_file:
        out_file.write(sessions.content)
