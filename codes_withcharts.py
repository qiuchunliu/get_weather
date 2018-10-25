# CREATED FOR TEST 1

# 获取天气信息
import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
#
area = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn']
# 构造地区列表，用于后续的url
urllist = []
# url列表
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
            #     print('城市：{0:<15} {1:>4}：{2:>5}'.format(tr.find('td', width=83).a.string, '温度',
            #                                             tr.find('td', width=86).string), chr(12288))
            content.append({'城市': tr.find('td', width=83).a.string, '温度': tr.find('td', width=86).string})


content = []
# 创建一个列表，存放键值对
# 保存每个城市和其最低温度
# 这样的话，所有信息可以存在列表里
for each in urllist[:2]:
    result(each)


t = content[:7]

# 可以用函数来写
# def f(data):
#     minp = data['温度']
#     return minp

# 也可以直接用 lambda 表达式来写
t.sort(key=lambda dic: int(dic['温度']))
# print(t)

# 可以取 GitHub 上找摸板的
# CtrlC + CtrlV
attr = [city['城市'] for city in t]
v1 = [temp['温度'] for temp in t]
bar = Bar("低温排行")
bar.add("温度", attr, v1, is_stack=True)
