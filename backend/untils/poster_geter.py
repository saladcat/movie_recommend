from lxml import etree
import requests
from urllib import request


def get_poster_src(url):
    html = request.urlopen(url).read().decode('utf-8')
    html = etree.HTML(html)
    datas = html.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/a/img')
    ret_src = 'http://www.wenbao.net/new28/images/fzts.jpg'
    if len(datas) > 0:
        node = datas[0]
        node: etree._Element
        ret_src = node.get('src')
    return ret_src


if __name__ == '__main__':
    print(get_poster_src("https://www.imdb.com/title/tt1537787/"))
