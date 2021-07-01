#国内各省疫情情况
import requests
import re


def parse_url(page_url,f):

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    try:
        r=requests.get(page_url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        html = r.text
    except:
        print('访问失败')

    # print(html)
    #获取省或城市的信息，为避免遗漏省份，可以先将"provinceShortName"替换"cityName"再分析
    #html = re.sub(r'title', 'titles', html)
    #再把关于中国的部分取出来
    html=re.search('{ window.getTimelineService1 =.+?window.getIndexRecommendList2',html)

    html=html.group()
    # print(html)
    bobaos=re.findall(r"""
    {.*?"title":"(.+?)"
    """,html,re.VERBOSE|re.DOTALL)

    # print(type(cities))
    for bobao in bobaos:
        bobao=list(bobao)
        # print(city)
        f.write('{}\n'.format(''.join(bobao[0])))


def main():
    page_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    with open('epidemic bobao.csv', 'a', encoding='utf-8') as f:
        parse_url(page_url,f)
main()