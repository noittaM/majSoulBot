from sys import argv
import json

from bot import client

if len(argv) < 2:
    raise Exception('No config provided')

config_path = argv[1]
config = json.load(open(config_path, "r"))

if 'token' not in config:
    raise Exception('No token')

token = config['token']

client.run(token)
