# Urllib是python内置的HTTP请求库  包括
# urllib.request 请求模块
# urllib.error 异常处理模块
# urllib.parse url解析模块
# urllib.robotparser robots.txt解析模块


# urllib.request.urlopen参数的介绍：
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))


# 通过bytes(urllib.parse.urlencode())可以将post数据进行转换放到urllib.request.urlopen的data参数中,完成一次post请求。
# 所以如果我们添加data参数的时候就是以post请求方式请求，如果没有data参数就是get请求方式
import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data)
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())


# timeout参数:在某些网络情况不好或者服务器端异常的情况会出现请求慢的情况,或者请求异常,
# 所以这个时候我们需要给请求设置一个超时时间,而不是让程序一直在等待结果。
import socket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


# 响应类型、状态码、响应头
# 可以通过response.status,response.getheaders(),response.getheader("server"),获取状态码以及头部信息
# response.read()获得的是响应体的内容
import urllib.request
response = urllib.request.urlopen('https://www.python.org')
print(type(response))


# 有很多网站为了防止程序爬虫爬网站造成网站瘫痪,会需要携带一些headers头部信息才能访问
from urllib import request, parse
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {'name': 'zhangmenghan'}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# 第二种添加请求头的方式
from urllib import request, parse
url = 'http://httpbin.org/post'
dict = {
    'name': 'zhangmenghan'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))


# 通过rulllib.request.ProxyHandler()可以设置代理,网站它会检测某一段时间某个IP 的访问次数,
# 如果访问次数过多,它会禁止你的访问,所以这个时候需要通过设置代理来爬取数据
import urllib.request
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read())


# cookie中保存中我们常见的登录信息,有时候爬取网站需要携带cookie信息访问,这里用到了http.cookijar,
# 用于获取cookie以及存储cookie
import http.cookiejar
import urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)


# http.cookiejar.MozillaCookieJar()方式写入到文件中保存
import http.cookiejar
import urllib.request
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)


# http.cookiejar.LWPCookieJar()方式写入到文件中保存
import http.cookiejar
import urllib.request
filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)


# 获取文件中的cookie获取的话可以通过load方式，用哪种方式写入的，就用哪种方式读取(在这里是LWPCookieJar())。
import http.cookiejar
import urllib.request
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))

# 异常处理
# URLError里只有一个属性：reason,即抓异常的时候只能打印错误信息
from urllib import request,error
try:
    response = request.urlopen("http://pythonsite.com/1111.html")
except error.URLError as e:
    print(e.reason)


# HTTPError里有三个属性：code,reason,headers，即抓异常的时候可以获得code,reson，headers三个信息
from urllib import request,error
try:
    response = request.urlopen("http://pythonsite.com/1111.html")
except error.HTTPError as e:
    print(e.reason)
    print(e.code)
    print(e.headers)
except error.URLError as e:
    print(e.reason)

else:
    print("reqeust successfully")


# e.reason也可以在做深入的判断
import socket

from urllib import error,request

try:
    response = request.urlopen("http://www.pythonsite.com/",timeout=0.001)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print("time out")


# URL解析
# urlparse 对你传入的url地址进行拆分
from urllib.parse import urlparse
result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(result)


# urlunpars  功能和urlparse的功能相反，它是用于拼接
from urllib.parse import urlunparse
data = ['http','www.baidu.com','index.html','user','a=123','commit']
print(urlunparse(data))


# urljoin  这个函数的功能是做拼接的(从拼接的结果我们可以看出，拼接的时候后面的优先级高于前面的url)
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))


# urlencode 这个方法可以将字典转换为url参数
from urllib.parse import urlencode
params = {
    "name":"zhaofan",
    "age":23,
}
base_url = "http://www.baidu.com?"

url = base_url+urlencode(params)
print(url)
