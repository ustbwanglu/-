# import urllib.request
# import urllib.parse
# import json
# import sys
#
# content = input("请输入翻译内容")
# print("\n")
#
# url =
#
# import time
# import hashlib
# import requests
# import random
#
# class Youdao():
#
#     def __init__(self):
#
#         self.lan_dict={
#             '中文':'zh-CHS',
#             '英文': 'en',
#             '俄文': 'ru',
#             '法文': 'fr',
#             '日文': 'ja',
#             '韩文': 'ko'
#             }
#         self.s = requests.Session()
#         self.s.keep_alive = False
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
#             'Referer': 'http://fanyi.youdao.com/',
#             'contentType': 'application/x-www-form-urlencoded; charset=UTF-8',
#             'Cookie': 'OUTFOX_SEARCH_USER_ID=-352392290@116.136.20.84; P_INFO=a121bc; OUTFOX_SEARCH_USER_ID_NCOO=710017829.1902944; JSESSIONID=aaaDa3sqezCDY-snjj91w; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=' + str(
#                 int(time.time() * 1000)),
#         }
#         self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#
#     def translate(self,from_lan,to_lan,text):
#         self.headers['Content-Length'] = str(233 + len(text))
#         ts = str(int(time.time() * 1000))
#         salf = ts + str(random.randint(0, 9))
#         n = 'fanyideskweb' + text + salf + "n%A-rKaT5fb[Gy?;N5@Tj"
#         self.m = hashlib.md5()
#         self.m.update(n.encode('utf-8'))
#         sign = self.m.hexdigest()
#         data = {
#             'i': text,
#             'from': from_lan,
#             'to': to_lan,
#             'smartresult': 'dict',
#             'client': 'fanyideskweb',
#             'salt': salf,
#             'sign': sign,
#             'ts': ts,
#             'bv': '53539dde41bde18f4a71bb075fcf2e66',
#             'doctype': 'json',
#             'version': "2.1",
#             'keyfrom': "fanyi.web",
#             'action': "FY_BY_REALTlME"
#         }
#         try:
#             result = self.s.post(self.url, headers=self.headers, data=data, timeout=5).json()
#             if result != None:
#                 ans = result['translateResult'][0][0]['tgt']
#                 return ans
#             else:
#                 return None
#         except Exception as e:
#             return None
#
# if __name__ == '__main__':
#
#         yd = Youdao()
#         text = 'hello'
#         print(yd.translate('zh-CHS','en',text))


# import time, math, random, hashlib
# import requests
#
#
# def get_html(name):
#     url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#
#     ts = math.floor(time.time() * 1000)
#     salt = ts + int(random.random() * 10)
#
#     sign = hashlib.md5(("fanyideskweb" + name + str(salt) + "Nw(nmmbP%A-r6U3EUn]Aj").encode('utf-8')).hexdigest()
#     bv = hashlib.md5((
#                          "5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0").encode(
#         'utf-8')).hexdigest()
#
#     data = {
#         'i': name,
#         'from': 'AUTO',
#         'to': 'AUTO',
#         'smartresult': 'dict',
#         'client': 'fanyideskweb',
#         'salt': salt,
#         'sign': sign,
#         'ts': ts,
#         'bv': bv,
#         'doctype': 'json',
#         'version': '2.1',
#         'keyfrom': 'fanyi.web',
#         'action': 'FY_BY_CLICKBUTTION',
#     }
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
#         'Referer': 'http://fanyi.youdao.com/',
#         # 参考链接:http://fanyi.youdao.com/
#         # 请在此处填写你的 Cookie
#     }
#
#     html = requests.post(url, headers=headers, data=data)  # 有需要的可以改成session写法
#     # print(html.json())
#     print('正在执行有道翻译程序:')
#     print('翻译的词:{}'.format(html.json()['translateResult'][0][0]['src']))
#     print('翻译结果:{}'.format(html.json()['translateResult'][0][0]['tgt']))
#
#
# if __name__ == "__main__":
#     name = '靓仔'
#
#     get_html(name)
import urllib.request
import urllib.parse
import json

def translate(content):
    f=content
    h={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
    d={"i":f,"from":"AUTO","to":"AUTO","smartresult":"dict","client":"fanyideskweb","salt":"15783143482231","sign":"acc6872ebb674de2ec8c5c2a941ad1be","ts":"1578314348223","bv":"e2a78ed30c66e16a857c5b6486a1d326","doctype":"json","version":"2.1","keyfrom":"fanyi.web","action":"FY_BY_CLICKBUTTION"}
    d=urllib.parse.urlencode(d).encode('utf-8')
    r=urllib.request.Request('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule',d,h)
    i=urllib.request.urlopen(r)
    a=i.read().decode('utf-8')
    b=json.loads(a)
    b=b['translateResult'][0][0]['tgt']
    return b

#
# b=translate("我是英雄")
# print('翻译的结果'+b)