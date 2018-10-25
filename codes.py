# CREATED FOR TEST 1

import requests
from bs4 import BeautifulSoup

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
#
area = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
urllist = []
for ar in area:
    urllist.append('http://www.weather.com.cn/textFC/{}.shtml'.format(ar))
# # print(urllist)


def result(url):

    res = requests.get(url, headers=head)
    res.encoding = 'utf-8'
    resoup = BeautifulSoup(res.text, 'lxml')
    # print(resoup.prettify())
    # print(resoup.find('div', class_='conMidtab').find_all('div', class_='conMidtab2')[0].table)
    provinces = resoup.find('div', class_='conMidtab').find_all('div', class_='conMidtab2')
    # 省份列表
    # print(resoup)
    for province in provinces:
        trs = province.find_all('tr')[2:]
        # [2:] ： 因为列表的前两项无用，表示去掉列表的前两个。
        for tr in trs:
            print('城市：{0:<15} {1:>4}：{2:>5}'.format(tr.find('td', width=83).a.string, '温度', tr.find('td', width=86).string), chr(12288))


for each in urllist:
    result(each)
