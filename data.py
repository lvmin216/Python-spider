import urllib
import urllib.request

data={}
data['word']='lvmin'

url = "http://www.baidu.com/s?"
url_values=urllib.parse.urlencode(data)
full_url=url+url_values
print(full_url)

data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)
