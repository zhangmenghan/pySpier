# re.match() 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
# 语法格式：re.match(pattern,string,flags=0)
import re
content = "hello 123 4567 World_This is a regex Demo"
result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
print(result)
print(result.group())
print(result.span())


# result.group()获取匹配的结果
# result.span()获去匹配字符串的长度范围
# 泛匹配
import re
content= "hello 123 4567 World_This is a regex Demo"
result = re.match("^hello.*Demo$",content)
print(result)
print(result.group())
print(result.span())


# 匹配目标,如果为了匹配字符串中具体的目标，则需要通过（）括起来
import re
content= "hello 1234567 World_This is a regex Demo"
result = re.match('^hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())


# 贪婪匹配
import re
content= "hello 1234567 World_This is a regex Demo"
result= re.match('^hello.*(\d+).*Demo',content)
print(result)
print(result.group(1))


# 匹配模式 匹配的内容是存在换行的问题的,这个时候的就需要用到匹配模式re.S来匹配换行的内容
import re
content = """hello 123456 world_this
my name is zhaofan
"""
result =re.match('^he.*?(\d+).*?zhaofan$', content, re.S)
print(result)
print(result.group())
print(result.group(1))


# 转义
import re
content = "price is $5.00"
result = re.match('price is \$5\.00',content)
print(result)
print(result.group())

# 尽量使用泛匹配,使用括号得到匹配目标,尽量使用非贪婪模式,有换行符就用re.S


html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''


# re.search扫描整个字符串返回第一个成功匹配的结果
import re
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(result.groups())
print(result.group(1))
print(result.group(2))


# re.findall搜索字符串,以列表的形式返回全部能匹配的子串
import re
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])


# re.sub替换字符串中每一个匹配的子串后返回替换后的字符串
import re
content = "Extra things hello 123455 World_this is a regex Demo extra things"
content = re.sub('(\d+)',r'\1 7890', content)
print(content)


# re.compile将正则表达式编译成正则表达式对象,方便复用该正则表达式
import re
content = """hello 12345 world_this
fan
"""
pattern = re.compile("hello.*fan", re.S)
result = re.match(pattern, content)
print(result)
print(result.group())


# 正则的综合练习
# 获取豆瓣网书籍的页面的书籍信息,通过正则实现
import requests
import re
content = requests.get('https://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
print(results)
for result in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)
