# -*- coding: utf-8 -*-

import time
import random
import itchat

def debug_1(msg): 
    print('FromUserName: ' + msg.FromUserName + '\n')
    print('ToUserName: ' + msg.ToUserName + '\n')
    print('User.NickName: ' + msg.User.NickName + '\n')
    return 1
def delay_1(t1, t2): 
    time.sleep(random.randrange(t1, t2)/1000)
    return 1

@itchat.msg_register(itchat.content.TEXT)
def text_print(msg): 

    if msg.User.UserName == msg.FromUserName: 
        print('\n' + msg.User.NickName + ' Sent You Message:  ' + msg.Text + '\n')
    else: 
        print('\nYou Sent  ' + msg.User.NickName + ' Message:  ' + msg.Text + '\n')

    delay_1(100, 500)
    debug_1(msg)
    return 1

itchat.auto_login(hotReload = True,enableCmdQR = True)
itchat.run()