import os
from dotenv import load_dotenv
from json import load, dump

load_dotenv()

DATABASE =os.getenv('DATABASE')

def create():
 if not os.path.isfile(DATABASE) or os.path.getsize == 0:
        with open(DATABASE, 'w+') as file:
           dump([], file, indent=2)

def read():
    with open(DATABASE, "r") as json_file:
        return load(json_file)

def verify(database, email):
    for user in database:
        if user["email"] == email:
            return False
        return True
