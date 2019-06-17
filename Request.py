# requests简单演示
import requests
response = requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
print(response.content)
# 返回的数据格式是二进制格式,通过decode()转换为utf-8编码，解决了通过response.text直接返回显示乱码的问题
print(response.content.decode("utf-8"))

# 或者
# response = requests.get("http://www.baidu.com")
# response.encoding = "utf-8"
# print(response.text)


# 基本GET请求
import requests
response = requests.get('http://httpbin.org/get')
print(response.text)


# 带参数的GET请求
import requests
response = requests.get("http://httpbin.org/get?name=zhaofan&age=23")
print(response.text)


# Requests模块允许使用params关键字传递参数，以一个字典来传递这些参数
import requests
data = {
    "name":"zhaofan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.url)
print(response.text)


# 解析json
import requests
import json
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))


# 添加headers
import requests
headers = {

    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response = requests.get("https://www.zhihu.com", headers=headers)
print(response.text)


# 基本POST请求(字典形式)
import requests
data = {
    "name":"zhaofan",
    "age":23
}
response = requests.post("http://httpbin.org/post", data=data)
print(response.text)


# 响应 可以通过response获得很多属性
import requests
response = requests.get("http://www.baidu.com")
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)

# 状态码判断,Requests还附带了一个内置的状态码查询对象
# 具体见https: // blog.csdn.net / museyouxia / article / details / 92707930
import requests
response= requests.get("http://www.baidu.com")
if response.status_code == requests.codes.ok: # 200: ('ok'),
    print("访问成功")


# 文件上传
import requests
files= {"files":open("git.jpeg","rb")}
response = requests.post("http://httpbin.org/post",files=files)
print(response.text)


# 获取cookie
import requests
response = requests.get("http://www.baidu.com")
print(response.cookies)

for key,value in response.cookies.items():
    print(key+"="+value)


# 使用cookie模拟登陆，做会话维持
import requests
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456")
response = s.get("http://httpbin.org/cookies")
print(response.text)


# 证书验证
import requests
import urllib3
urllib3.disable_warnings()
response = requests.get("https://www.12306.cn", verify=False)
print(response.status_code)


# 代理设置
import requests
proxies= {
    "http":"http://127.0.0.1:9999",
    "https":"http://127.0.0.1:8888"
}
response = requests.get("https://www.baidu.com", proxies=proxies)
print(response.text)


# 认证设置
import requests
from requests.auth import HTTPBasicAuth
response = requests.get("http://120.27.34.24:9001/",auth=HTTPBasicAuth("user", "123"))
print(response.status_code)

# 另外一种认证设置
import requests
response = requests.get("http://120.27.34.24:9001/",auth=("user", "123"))
print(response.status_code)


# 异常处理,详细见http://www.python-requests.org/en/master/api/#exceptions
import requests
from requests.exceptions import ReadTimeout,ConnectionError,RequestException
try:
    response = requests.get("http://httpbin.org/get",timout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection Error")
except RequestException:
    print("error")
