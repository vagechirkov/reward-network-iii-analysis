# reward-network-iii-analysis

## Virtual Environment

```bash
python3 -m venv venv
 
source venv/bin/activate

python3 -m pip install --upgrade pip

```

## Setup .env

You need to create a .env file in the root directory of the project. The .env
file should contain the following variables:

```dotenv
BACKEND_USER=<your backend user>
BACKEND_PASSWORD=<your backend password>
BACKEND_URL=<your backend url>
```

## Downloading the data

```bash

python3 download_data.py

```

