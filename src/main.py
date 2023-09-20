from sys import argv
import json
import os

from dotenv import load_dotenv
from bot import client

load_dotenv("../.env")
if len(argv) < 2:
    raise Exception('No config provided') 
   

config_path = argv[1]
config = json.load(open(config_path, "r"))

if 'token' not in config:
    #raise Exception('No token') isn't the point of this is that the program keeps running even after running into a problem?
    token = os.environ.get('BOT_TOKEN')
else:
    token = config['token']

client.run(token)
