import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


url = "http://www.baidu.com"
html = getHtml(url)

print(html)
