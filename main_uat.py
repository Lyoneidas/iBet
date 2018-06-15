import itchat
import json
import re
from itchat.content import TEXT

WCG_uat = ''

wcg_welcome = '''
给参加测试的各位大爷们磕头了
现在版本为alpha 0.0.1
大爷们常来玩儿啊！
--------------------------
已开放功能:
++hello: 会回复欢迎信息，也能加个名儿如 ++hello: Alan
++h: 列出所有命令(注意是不是available的)
++teams: 列出所有参赛队，也可以加参数如: ++teams: A 显示A组球队
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
    if chatroom_id == WCG_uat:
        if msg.isAt:
            ret = '大熊弟你就摇了我吧这功能妹时间做啊！'
            content = msg.Content.strip()
            # print('Message received: ', content)
            if "++" in content:
                cmd_str = re.match('^@Alan\s*Tu\s*\+\+' + pattern + '\:?(.*)', content).group(1)
                cmd = wcg_commands.get(cmd_str)
                if len(re.match('^@Alan\s*Tu\s*\+\+' + pattern + '\:?(.*)', content).groups()) > 2 and cmd['method_param']:
                    ret = cmd['method_param'](re.match('^@Alan\s*Tu\s*\+\+' + pattern + '\:?(.*)', content).group(2))
                elif cmd['implemented']:
                    ret = cmd['method']()
            itchat.send(ret, WCG_uat)

itchat.auto_login(hotReload = True)
chatrooms = itchat.search_chatrooms(name='Chatbot UAT')
if len(chatrooms) == 1:
    WCG_uat = chatrooms[0]['UserName']
itchat.send(wcg_welcome, WCG_uat)

itchat.run()
