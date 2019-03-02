import urllib.request 
from bs4 import BeautifulSoup
import lxml
import html5lib
import pandas as pd
from datetime import datetime

def get_tenki_jp(now):
    ##気象協会
    url = 'https://tenki.jp/forecast/3/16/4410/13103/'
    dfs = pd.read_html(url,encoding='utf-8')    
    df = dfs[0].head()
    data = df.at[0,now]
    return data

def get_weather_news():
    url = 'https://www.google.com/search?q=%E6%B8%AF%E5%8C%BA+%E9%99%8D%E6%B0%B4%E7%A2%BA%E7%8E%87&oq=%E6%B8%AF%E5%8C%BA%E3%80%80%E9%99%8D%E6%B0%B4%E7%A2%BA%E7%8E%87&aqs=chrome..69i57j0l5.9041j1j4&sourceid=chrome&ie=UTF-8'
    res = urllib.request.urlopen(url)
    weather = "-"
    soup = BeautifulSoup(res,'html.parser')
    for i,div_element in enumerate(soup.findAll("div",class_="wob_pp")):
        print(i,div_element)
        if(div_element != None):
            pass
        else:
            weather = div_element

        print(weather)

def get_jma(now):
    ##
    url = 'https://www.jma.go.jp/jp/yoho/319.html'
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res,'html.parser')
    table = soup.findAll("table",class_="rain")[0]
    tds = table.findAll("td")
    col = []
    for td in tds:
        col.append(str(td).replace("<td align=\"right\">","").replace("<td align=\"left\">","").replace("</td>",""))
    if now in col :
               precipitation = col[col.index(now) + 1 ] 
    return precipitation


now = datetime.now().strftime("%H")
now = int(now)
if 0 <= now < 6:
    now = '00-06'
elif 6 <= now < 12:
    now = '06-12'
elif 12 <= now < 18:
    now = '12-18'
elif 18 <= now < 24:
    now = '18-24'


data = get_tenki_jp(now)
print(data)

data2 = get_jma(now)
print(data2)