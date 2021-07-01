import requests,json
url='https://app2bqyqmmn9504.h5.xiaoeknow.com/v1/course/video/v_5f4e623ce4b0158ded4db85e?type=2&pro_id=p_5f195e3fe4b0a1003caebe2f&from_multi_course=1 '
header={
    'Cache-Control': 'max-age=0',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
    'X-Requested-With':'XMLHttpRequest',
    'Content-Length':'185',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://appl0u0rcfq7859.h5.xiaoeknow.com/evaluation_wechat/practice/enter/wb_5e6fa59c8c845_cz016qLq',
    'Origin': 'https://appl0u0rcfq7859.h5.xiaoeknow.com',
    'Host': 'appl0u0rcfq7859.h5.xiaoeknow.com'
}
Cookie='ko_token=**********************;\
sajssdk_2015_cross_new_user=1;\
sa_jssdk_2015_appl0u0rcfq7859=%7B%22distinct_id%22%3A%22u_5e53690c59efc_MyN7iue94u%22%2C%22%24device_id%22%3A%22170fad24486507-0b3393d5380542-8011274-2073600-170fad24487437%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22170fad24486507-0b3393d5380542-8011274-2073600-170fad24487437%22%7D;\
Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1584756049;\
Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1584766252;\
sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170fad24486507-0b3393d5380542-8011274-2073600-170fad24487437%22%2C%22%24device_id%22%3A%22170fad24486507-0b3393d5380542-8011274-2073600-170fad24487437%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D;\
dataUpJssdkCookie={"wxver":"7.0.5","net":"WIFI","sid":"1584756049206_merhds"};\
bizData%5Bresource_id%5D=wb_5e6fa59c8c845_cz016qLq&bizData%5Bpage%5D=1&bizData%5Bpage_size%5D=10&bizData%5Btype%5D=practice'
Cookie=Cookie.split(';')
dict={}
for i in Cookie:
    a=i.split('=')
    dict[a[0]]=a[1]
print(dict)
data = {
    'bizData[resource_id]':'wb_5e6fa5e192213_FtUmTibP',
    'bizData[page_size]':100,
    'bizData[type]':'practice'
}
res=requests.post(url,headers=header,params=dict,data=data,verify=False)
a=res.json()
with open("F:/BaiduNetdiskDownload","w") as f:
    json.dump(a,f)
    print("加载入文件完成...")
