
   
###################################################################   8
#
#print(b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'.decode('utf-8'))
#
###################################################################

###################################################################   7
#import re
#import requests
#
#wid = 40
#print('*' * wid)
#print('Name' + '\0' * (wid - 9) + 'Price')
#print('-' * wid)
#
#url = 'https://book.douban.com/top250?icn=index-book250-all'
#resp = requests.get(url)
#content = resp.text
#
#res = re.findall('le="(\w+)".*?pl">(.*?)\s/.*?(\d+\.\d+)', content, re.S)
#
#for i in range(len(res)):
#    n_len = len(list(res[i][0])) + len(re.findall('(\w)', res[i][0], re.A))
#    print('{{:{}}}{{:>{}.2f}}'.format(29 - n_len, 10).format(res[i][0], float(res[i][2])))
#
#print('*' * wid)
#
#print(res)
#
# '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width).format(results[0][0],float(results[0][1]))
#
###################################################################

###################################################################   6
#def a_new_decorator(a_func):
# 
#    def wrapTheFunction():
#        print("I am doing some boring work before executing a_func()")
# 
#        a_func()
# 
#        print("I am doing some boring work after executing a_func()")
# 
#    return wrapTheFunction
# 
#def a_function_requiring_decoration():
#    print("I am the function which needs some decoration to remove my foul smell")
#
#print(a_function_requiring_decoration.__name__)
# 
#a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"
# 
#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()
# 
#a_function_requiring_decoration()
#
#print(a_function_requiring_decoration.__name__)
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()
#
###################################################################

###################################################################   5
#import time
#import random
#import itchat
#
#def debug_1(msg): 
#    print('FromUserName: ' + msg.FromUserName + '\n')
#    print('ToUserName: ' + msg.ToUserName + '\n')
#    print('User.NickName: ' + msg.User.NickName + '\n')
#    return 1
#def delay_1(t1, t2): 
#    time.sleep(random.randrange(t1, t2)/1000)
#    return 1
#
#@itchat.msg_register(itchat.content.TEXT)
#def text_print(msg): 
#
#    if msg.User.UserName == msg.FromUserName: 
#        print('\n' + msg.User.NickName + ' Sent You Message:  ' + msg.Text + '\n')
#        if msg.User.NickName == 'YTong_': 
#            if '傻' in msg.Text: 
#                delay_1(200, 1500)
#                itchat.send('Jerry最傻', toUserName = msg.FromUserName)
#    else: 
#        print('\nYou Sent  ' + msg.User.NickName + ' Message:  ' + msg.Text + '\n')
#    
#    delay_1(100, 500)
#    debug_1(msg)
#    return 1
#
#itchat.auto_login(hotReload = True,enableCmdQR = True)
#itchat.run()
###################################################################

###################################################################   4
#import time
#file = open('D:\\1.txt','w')
#for i in range(100000000):
#    file.write('{:08}\n'.format(i))
#file.close()
#print()
#print('Finish at ' + time.ctime() + '\n')
#
###################################################################

###################################################################   3
#
#def fibs(num):
#    fib = [0,1]
#    for i in range(num - 2):
#        fib.append(fib[-2] + fib[-1])
#    return fib
#
#num = list(range(1,11))
#i = int(input('Press enter i: '))
#
#print(num)
#print(fibs(i))
#
#print(num + fibs(i))
#
#for t in range(2):
#    print('a')
#    for t in range(2):
#        print('b')
#    print('c\n')
###################################################################

###################################################################   2
#people = {
#    'Alice':{'phone': '2341',
#             'addr': 'Foo drive 23'},
#    'Beth': {'phone': '9102',
#             'addr': 'Bar street 42'}
#    }
#
#labels = {'phone': 'phone number',
#         'addr': 'address'}
#
#name = input('Name: ')
#
# 要查找电话号码还是地址？
#request = input('Phone number (P) or Address (A)? ')
#
# 使用正确的键：
#key = request
#if request == 'P': key = 'phone'
#if request == 'A': key = 'addr'
#
# 使用get提供默认值
#person = people.get(name, {})
#print(person)
#label = labels.get(key, key)
#result = person.get(key, 'not available')
#print("{}'s {} is {}.".format(name, label, result))
###################################################################

###################################################################   1
#import math

#print('\n\0Hello World!\n\0Let\'s Go!\n')

#month = ['Januray','February','March','April','May','June','July'
#       ,'August','September','October','November','December']

#yyyy = input('请输入年=')
#mm = int(input('请输入月='))-1
#dd = input('请输入日=')

#print('当前日期是:' + yyyy + '\\' + month[mm] + '\\' + dd)

#a1 = input('输入4位数: ')
#a2 = input('输入4位数: ')
#a1 = list(a1)
#a2 = list(a2)

#b1 = sorted(a1)
#b2 = a2.copy()
#b2.sort(reverse = True)
#print(b1)
#print(b2)
#print('%d的%d次方=%d' %( int(b1[0]), int(b2[0]),pow(int(b1[0]),int(b2[0]) 
#                                                   )
#                       )
#     )
###################################################################