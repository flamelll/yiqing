from lxml import etree
from selenium import webdriver

def get_cities(url):
    cities=[]
    try:
        driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
        driver.get(url)
        text = driver.page_source
    except:
        print('访问失败')
    html = etree.HTML(text)
    tbodys = html.xpath('//*[@id="listWraper"]/table[2]/tbody')
    for tbody in tbodys:
        trs = tbody.xpath('./tr')
        cities.extend(trs)
    return cities

def parse_city(city):
    area =city.xpath("string(./th)")
    Today_confirmed = city.xpath("string(./td[2]/p[2])").strip()
    Existing_confirmed = city.xpath('string(./td[1])').strip()
    try:
        cumulative_confirmed= city.xpath('./td[2]//text()')[0].strip()
    except:
        cumulative_confirmed=''
    cure = city.xpath('string(./td[3])').strip()
    dead = city.xpath('string(./td[4])').strip()
    data = {}
    data['Today_confirmed']=Today_confirmed
    data['dead']=dead
    data['cure']=cure
    data['cumulative_confirmed']=cumulative_confirmed
    data['area']=area
    data['Existing_confirmed']=Existing_confirmed
    return data

def sava_data(data,f):
    f.write('{},{},{},{},{},{}\n'.format(data['area'],data['Today_confirmed'],data['Existing_confirmed'],data['cumulative_confirmed'],data['cure'],data['dead']))
    print('ok')

def main():
    with open('Domestic outbreak cities in China.csv','a',encoding='utf-8') as f:
        url="https://news.qq.com/zt2020/page/feiyan.htm#/?nojump=1"
        cities=get_cities(url)
        for city in cities:
            data=parse_city(city)
            sava_data(data,f)

main()