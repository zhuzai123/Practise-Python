# -*- coding: utf-8 -*-

import re
import requests

wid = 40
print('*' * wid)
print('Name' + '\0' * (wid - 9) + 'Price')
print('-' * wid)

url = 'https://book.douban.com/top250?icn=index-book250-all'
resp = requests.get(url)
content = resp.text

res = re.findall('le="(\w+)".*?pl">(.*?)\s/.*?(\d+\.\d+)', content, re.S)

for i in range(len(res)):
   n_len = len(list(res[i][0])) + len(re.findall('(\w)', res[i][0], re.A))
   print('{{:{}}}{{:>{}.2f}}'.format(29 - n_len, 10).format(res[i][0], float(res[i][2])))

print('*' * wid)

print(res)