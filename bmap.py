from pyecharts.charts import BMap
# from example.commons import Faker
from pyecharts.faker import Faker
from pyecharts import options as opts
import json
import requests
import os
from selenium import webdriver

output='json'
ak='Z2hzbMkqq4hgAS0IPHgRYPoRfjP9QBee'
url = 'http://api.map.baidu.com/place/v2/search?q=华中科技大学食堂&region=武汉&output='+output+'&ak='+ak
r = requests.get(url)
r_js = r.json()
for i in range(0, 9):
    names = r_js['results'][i]['name']
    lng_ = r_js['results'][i]['location']['lng']
    lat_ = r_js['results'][i]['location']['lat']
    print(names, lng_, lat_)


c = BMap()
c.width = "1000px"
c.height = "800px"
c.add_schema(
            baidu_ak='Z2hzbMkqq4hgAS0IPHgRYPoRfjP9QBee',
            center=[114.421214, 30.519139], zoom=17

        )
for i in range(0, 9):
    c.add_coordinate(r_js['results'][i]['name'], r_js['results'][i]['location']['lng'], r_js['results'][i]['location']['lat'])
    c.add("华中科技大学食堂", [(r_js['results'][i]['name'], "#404a59")], color="#404a59")
c.set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"), visualmap_opts=opts.VisualMapOpts(is_piecewise=True))
c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
c.render()

'''driver = webdriver.Chrome()
driver.get("F:///pyecharts/untitled/html/road.html")
driver.get("http://127.0.0.1:8848/untitled/road.html")'''