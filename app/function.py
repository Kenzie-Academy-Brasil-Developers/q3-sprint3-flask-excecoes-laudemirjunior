import os
from json import dump
from dotenv import load_dotenv
from json import dump
from .exception import EmailError
from .assistant import verify

load_dotenv()

DATABASE =os.getenv('DATABASE')

def add(request_user ,database, user):
  
    if verify(database, request_user['email']):
        raise EmailError

    else:
        database.append(user)
        with open(DATABASE, "w") as json_file:
            dump(database, json_file, indent=2)
