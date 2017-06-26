import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)

a = urllib.request.urlopen(url)
print(type(a))
print(a.geturl())
print(a.info())
print(a.getcode())