import itchat
import json
import re
from itchat.content import TEXT

WCG = ''

wcg_welcome = '''
Welcome to use iBet Chatbot
---------------------------
HOT-TO:
@Alan Tu ++<your command here>

EXAMPLE:

@Alan Tu ++h

This will list all the commands
'''
teams = {
    'A':{'Russia','Saudi Arabia','Egypt','Uruguay'},
    'B':{'Portugal','Spain','Morocco','Iran'},
    'C':{'France','Australia','Peru','Denmark'},
    'D':{'Argentina','Iceland','Croatia','Nigeria'},
    'E':{'Brazil','Switzerland','Costa Rica','Serbia'},
    'F':{'Germany','Mexico','Sweden','South Korea'},
    'G':{'Belgium','Panama','Tunisia','England'},
    'H':{'Columbia','Japan','Poland','Senegal'},
}

def hello():
    return "Hello from iBet Chatbot"

def hello_ha(name):
    return 'Hello ' + name + ' from iBet Chatbot'

def list_help():
    str = '''
    ++hello: print hello info, ++hello: <name> return hello with name | Available
    ++h: list all the available commands | Available
    ++ls: list all validate bets | Not Available
    ++order: place order, add order command behind | Not Available
    ++teams: list all team available, ++teams: <group> show teams in group A-H | Available'''
    return str

def list_teams():
    return teams

def get_teams(group):
    return teams.get(group)

wcg_commands = {
                    'hello':{'command': 'hello', 'implemented': True, 'method': hello, 'method_param': hello_ha},
                    'h':{'command': 'h', 'help': 'list all commands', 'implemented': True, 'method': list_help},
                    'ls':{'command': 'ls', 'help': 'list all bets', 'implemented': False},
                    'order':{'command': 'order', 'help': 'place order', 'implemented': False},
                    'teams':{'command': 'vs', 'help': 'show all available matches', 'implemented': True, 'method': list_teams, 'method_param': get_teams}
               }

pattern = '((?:h|ls|vs|teams))'

@itchat.msg_register(TEXT, isGroupChat=True)
def reply_bot(msg):
    # print('====Receive msg from: ' + msg['FromUserName'])
    chatroom_id = msg['FromUserName']
    username = msg['ActualNickName']
    if chatroom_id == WCG:
        if msg.isAt:
            ret = 'Error: Unsupported command'
            content = msg.Content.strip()
            if "++" in content:
                cmd_str = re.match('^\+\+' + pattern + '\:?(.*)', str).group(1)
                print('commnand received: ' + cmd_str)
                cmd = wcg_commands.get(cmd_str)
                if len(re.match('^\+\+' + pattern + '\:?(.*)', str).groups()) > 2 and cmd['method_param']:
                    ret = cmd['method_param'](re.match('^\+\+' + pattern + '\:?(.*)', str).group(2))
                elif cmd['implemented']:
                    ret = cmd['method']()
            itchat.send(ret, WCG)

itchat.auto_login(hotReload = True)
chatrooms = itchat.search_chatrooms(name='World Cup Prediction Market')
if len(chatrooms) == 1:
    WCG = chatrooms[0]['UserName']
itchat.send(wcg_welcome, WCG)

itchat.run()
