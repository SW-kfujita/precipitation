import urllib.request
from bs4 import BeautifulSoup
import lxml
import html5lib
import pandas as pd
from datetime import datetime


def get_tenki_jp(now):
    # 気象協会
    if now == '00-06':
        now = 1
    elif now == '06-12':
        now = 2
    elif now == '12-18':
        now = 3
    elif now == '18-24':
        now = 4

    url = 'https://tenki.jp/forecast/3/16/4410/13103/'
    dfs = pd.read_html(url, encoding='utf-8')
    df = dfs[0].head()
    data = df.at[1, now]
    print(data)
    return data.strip("%")


def get_weather_news():
    url = 'https://www.google.com/search?q=%E6%B8%AF%E5%8C%BA+%E9%99%8D%E6%B0%B4%E7%A2%BA%E7%8E%87&oq=%E6%B8%AF%E5%8C%BA%E3%80%80%E9%99%8D%E6%B0%B4%E7%A2%BA%E7%8E%87&aqs=chrome..69i57j0l5.9041j1j4&sourceid=chrome&ie=UTF-8'
    res = urllib.request.urlopen(url)
    weather = "-"
    soup = BeautifulSoup(res, 'html.parser')
    for i, div_element in enumerate(soup.findAll("div", class_="wob_pp")):
        print(i, div_element)
        if(div_element != None):
            pass
        else:
            weather = div_element

        print(weather)


def get_jma(now):
    ##
    url = 'https://www.jma.go.jp/jp/yoho/319.html'
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    table = soup.findAll("table", class_="rain")[0]
    tds = table.findAll("td")
    col = []
    for td in tds:
        col.append(str(td).replace("<td align=\"right\">", "").replace(
            "<td align=\"left\">", "").replace("</td>", ""))
    if now in col:
        precipitation = col[col.index(now) + 1]
    return precipitation.strip("%")
