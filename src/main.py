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

match (config.get['token'], os.environ.get('BOT_TOKEN')):
    case (None, env_token):
        token = env_token
    case (conf_token, _):
        token = conf_token
    case (_,_):
      raise Exception('No token')
    
client.run(token)
