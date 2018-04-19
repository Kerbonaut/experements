import urllib.request
import urllib.parse

inp = list(map(str, input().split()))
url = 'https://www.google.ru/search?q='
for i in inp:
    url += i + '+'
url += 'is'
prev_ans = ''
try:
    headers = {}
    headers['User-Agent'] = 'Mozilla/999.0'
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respdata = str(resp.read())
    while respdata.find('/url?q=') != -1:
        ansi = respdata.find('/url?q=') + 7
        ans = respdata[ansi:]
        ansi = ans.find('&amp;')
        respdata = respdata[ansi:]
        ans = ans[:ansi]
        if ans != prev_ans and not 'http://webcache.googleusercontent.com/search' in ans:
            print(ans)
        prev_ans = ans
except Exception as e:
    print(str(e))
