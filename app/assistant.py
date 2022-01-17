import os
from dotenv import load_dotenv
from json import JSONDecodeError, load, dump

load_dotenv()

DATABASE =os.getenv('DATABASE')

def create():
    try:
        with open(DATABASE, "r") as json_file:
            return load(json_file)
    except (FileNotFoundError, JSONDecodeError):
        with open(DATABASE, "w+") as json_file:
            dump([], json_file, indent=2)

def read():
    with open(DATABASE, "r") as json_file:
        return load(json_file)

def verify(database, email):
    print(database)
    for user in database:
        if user["email"] == email.lower():
            return True
    return False