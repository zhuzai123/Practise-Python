# -*- coding: utf-8 -*-

import math

print('\n\0Hello World!\n\0Let\'s Go!\n')

month = ['Januray', 'February', 'March', 'April', 'May', 'June', 'July', 
        'August', 'September', 'October', 'November', 'December']

yyyy = input('请输入年= ')
mm = int(input('请输入月= ')) - 1
dd = input('请输入日=')

print('当前日期是: ' + yyyy + '\\' + month[mm] + '\\' + dd)
