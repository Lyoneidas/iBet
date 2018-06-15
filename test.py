import re
import json
from operator import methodcaller

def list_help():
    str = '''
    ++h: list all the available commands
    ++ls: list all validate bets
    ++order: place order, add order command behind
    ++vs: list all available matches'''
    return str

wcg_commands = {
                    'h':{'command': 'h', 'help': 'list all commands', 'implemented': True, 'method': list_help},
                    'ls':{'command': 'ls', 'help': 'list all bets', 'implemented': False},
                    'order':{'command': 'order', 'help': 'place order', 'implemented': False},
                    'vs':{'command': 'vs', 'help': 'show all available matches', 'implemented': False}
               }
ds = [123,456]


def regex_test(input):
    pattern = '((?:h|ls|vs|order))'
    if '++' in input:
      print(re.match('\+\+(\w*)\:?(.*)', input).groups())


def get_switch(cmd):
    print(wcg_commands.get(cmd)['help'])

# help = wcg_commands.get('h')['method']()
