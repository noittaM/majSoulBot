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

match (config['token'], os.environ.get('BOT_TOKEN')):
    case (None, has_value):
        token = os.environ.get('BOT_TOKEN')
    case (has_value, _):
        token = config['token']
    case (_,_):
        Exception('No token')
    
client.run(token)
