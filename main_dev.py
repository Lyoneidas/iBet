import itchat
import json
import re
from itchat.content import TEXT

WCG_dev= ''

wcg_welcome = '''
to filehelper
你大爷的alpha 0.0.1
------------------------
'''
teams = [
    ['Russia','Saudi Arabia','Egypt','Uruguay'],
    ['Portugal','Spain','Morocco','Iran'],
    ['France','Australia','Peru','Denmark'],
    ['Argentina','Iceland','Croatia','Nigeria'],
    ['Brazil','Switzerland','Costa Rica','Serbia'],
    ['Germany','Mexico','Sweden','South Korea'],
    ['Belgium','Panama','Tunisia','England'],
    ['Columbia','Japan','Poland','Senegal']
]

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
    print(teams)
    return teams

def get_teams(group):
    return teams.get(group)

wcg_commands = {
                    'hello':{'command': 'hello', 'implemented': True, 'method': hello, 'method_param': hello_ha},
                    'h':{'command': 'h', 'help': 'list all commands', 'implemented': True, 'method': list_help},
                    'ls':{'command':'ls', 'help': 'list all bets', 'implemented': False},
                    'order':{'command': 'order', 'help': 'place order', 'implemented': False},
                    'teams':{'command': 'vs', 'help': 'show all available matches', 'implemented': True, 'method': list_teams, 'method_param': get_teams}
               }


@itchat.msg_register(TEXT, isGroupChat=False)
def reply_bot(msg):
    print(msg)
    if msg['ToUserName'] == 'filehelper':
        ret = '大熊弟你就摇了我吧这功能妹时间做啊！'
        content = msg.Content.strip()
        if "++" in content:
            matched = re.match('\+\+(\w*)\:?(.*)', content)
            cmd_str = matched.group(1)
            print('Command str: ', cmd_str)
            cmd = wcg_commands.get(cmd_str)
            if matched.group(2) != '' and cmd['method_param']:
                ret = cmd['method_param'](matched.group(2))
            elif cmd['implemented']:
                ret = cmd['method']()
        itchat.send(ret, toUserName='filehelper')

itchat.auto_login(hotReload = True)
# chatrooms = itchat.search_chatrooms(name='Chatbot UAT')
# if len(chatrooms) == 1:
#     WCG_uat = chatrooms[0]['UserName']
# itchat.send(wcg_welcome, WCG_uat)
itchat.send(wcg_welcome, toUserName='filehelper')

itchat.run()
