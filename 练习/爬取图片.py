import re
import urllib.request
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode(encoding = "UTF-8")
    return html
def getImg(html):
    reg = r'src="(.*\.jpg)"'
    imgre = re.compile(reg)
    imgList = re.findall(imgre,html)
    x = 0
    for i in imgList:
        urllib.request.urlretrieve(i,'c:\\Temp\\%s.png'%x)
        x+=1
html = getHtml("http://z.163.com/")
getImg(html)


