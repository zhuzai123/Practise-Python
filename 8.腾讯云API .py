# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac
import time
import requests

secret_id = 'a'
secret_key = 'a'

def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + '/?'
    query_str = '&'.join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str

def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode('utf-8'), s.encode('utf-8'), method).digest()
    return base64.b64encode(hmac_str)

if __name__ == '__main__':
    endpoint = 'cvm.tencentcloudapi.com'
    data = {
        'Action' : 'DescribeInstances',
        'InstanceIds.0' : 'ins-09dx96dg',
        'Limit' : 20,
        'Nonce' : 11886,
        'Offset' : 0,
        'Region' : 'ap-guangzhou',
        'SecretId' : secret_id,
        'Timestamp' : 1,
        'Version': '2017-03-12'
    }
    s = get_string_to_sign('GET', endpoint, data)
    data['Signature'] = sign_str(secret_key, s, hashlib.sha1)
    data['Timestamp']=int(time.time())
    print('Signature: \n' + data['Signature'])
    # 实际调用API
    resp = requests.get('https://' + endpoint, params=data)
    print(resp.url)
