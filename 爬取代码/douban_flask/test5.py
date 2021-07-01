import requests
from bs4 import BeautifulSoup
import json
import re
import codecs
# 1.发送请求，获取疫情首页

response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')  # <Response [200]>
home_page = response.content.decode()
# print(home_page)

# 2.从疫情首页，提取最近一日各国疫情数据
soup = BeautifulSoup(home_page, 'lxml')  # soup和home_page区别不大
script = soup.find(id="getListByCountryTypeService2true")
text = script.contents  # 以列表形式返回内容

# 3.从疫情数据中，获取json格式的字符串
json_str = re.findall(r'\[.+\]', text[0])[0]

# 4.把json格式的字符串转换为Python类型
last_day_corona_virus = json.loads(json_str)

# 5.以json格式保存最近一日各国疫情数据
with open('data/last_day_corona_virus.json', 'w') as fp:
    json.dump(last_day_corona_virus, fp, ensure_ascii=False)