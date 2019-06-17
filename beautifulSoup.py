from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p["class"])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))


# 获取名称
print(soup.title.name)

# 获取属性
print(soup.p.attrs['name'])
print(soup.p['name'])

# 获取内容
print(soup.p.string)

# 嵌套选择
print(soup.head.title.string)

# soup.a.children 子孙节点
# soup.a.parent 获取父节点
# soup.a.next_siblings 获取后面的兄弟节点
# soup.a.previous_siblings 获取前面的兄弟节点
# soup.a.next_sibling 获取下一个兄弟标签
# souo.a.previous_sinbling 获取上一个兄弟标签


# 标准选择器
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

# find_all(name,attrs,recursive,text,**kwargs)可以根据标签名,属性,内容查找文档
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))


# attrs
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))


# text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text='Foo'))


# find(name,attrs,recursive,text,**kwargs)返回的匹配结果的第一个元素
# find_parents()返回所有祖先节点，find_parent()返回直接父节点。
# find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
# find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
# find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
# find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点


# CSS选择器
# .表示class #表示id
# 标签1,标签2 找到所有的标签1和标签2
# 标签1 标签2 找到标签1内部的所有的标签2
# [attr] 可以通过这种方法找到具有某个属性的所有标签
# [atrr=value] 例子[target=_blank]
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))


# 通过get_text()就可以获取文本内容
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print(li.get_text())


# 获取属性
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
