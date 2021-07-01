import sys
import requests
import json
import pymysql
class yq():
    def __init__(self):
        self.load_url = "https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query={}&cb=jsonp_1586658326556_20322"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        self.tj = []

    # 1.发生请求
    def send_request(self, url):
        data = requests.get(url, headers=self.headers).content.decode("utf-8")
        return data

    # 2.解析数据
    def parse_jsondata(self, data,gj):
        i = data.find("(")+1
        data = data[i:-1]

        data = json.loads(data)
        if gj=='赞比亚共和国' or gj=='泽西岛' or gj=='根西岛' or gj=='也门共和国' or gj=='瓜德罗普岛' or gj=='蒙古' or gj=='荷属圣马丁' or gj=='布隆迪共和国' or gj=='格林那达' or gj=='北马里亚纳群岛联邦' or gj=='库拉索岛' or gj=='圣其茨和尼维斯' or gj=='福克兰群岛' or gj=='荷兰加勒比地区' or gj=='圣皮埃尔和密克隆群岛':
         print("iii")
        else:
            if data:
                # 存在值即为真
                qq = data["Result"][0]["DisplayData"]["result"]["items"]
                for i in qq:
                    a = {}
                    a["eventDescription"] = i["eventDescription"]
                    a["eventUrl"] = i["eventUrl"]
                    a["siteName"] = i["siteName"]
                    self.tj.append(a)
            else:
                # list_temp是空的
                print("该国家为空！")



    # 3.显示数据
    def show_data(self,gj,cj):
        a = 1
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='wangye')
        cur = conn.cursor()
        for i in self.tj:
            print(f'{a}.{i["eventDescription"]}     信息来源：{i["siteName"]}       链接：{i["eventUrl"]}     ')
            a=a+1
            title1 = f'{i["eventDescription"]}'
            link1 = f'{i["eventUrl"]}'
            source1 = f'{i["siteName"]}'
            if gj=='中国':
               cur.execute("insert into news(continents,provincename,title, link, source) values ('%s','%s','%s','%s','%s')"%(cj,gj,title1,link1,source1))
        conn.commit()
        cur.close()
        conn.close()
        # while True:
        #     print("*" * 125)
        #     try:
        #         list = int(input(f'请输入你要具体查看的新闻(如需重新查询国家，请输入0;如需保存所有数据，请输入{a};如需退出程序，请输入{a+1}):'))
        #         if (list == 0):
        #             self.run()
        #             break
        #         elif (list == a):
        #             print("保存文件格式为json文件，保存方法后续开发。。。")
        #             self.save_data()
        #         else:
        #             print(f'你要查看的新闻是：{self.tj[list - 1]["eventDescription"]}')
        #             print(f'信息来源：{self.tj[list - 1]["siteName"]}')
        #             print(f'具体内容：{self.tj[list - 1]["eventUrl"]}')
        #     except:
        #         if(list==a+1):
        #             print("*" * 125)
        #             print("程序结束,欢迎您再次使用！！！")
        #             print("如程序错误或与作者提出意见沟通交流，请加QQ：923534165，本人菜鸡，欢迎大家批判！！！")
        #             sys.exit()
        #         print("*" * 125)
        #         print("请输入正确字符")

    # 4.保存数据
    def save_data(self):
        json.dump(self.tj, open(f'{self.GJ}.json', "w"))


    # 5.启动
    def run(self):
        print("*" * 125)
        self.tj = []
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='vdata')
        cur = conn.cursor()
        cur.execute('select * from contury where date = "2020-05-26 00:00:00"')
        for users in cur.fetchall():
            print('continents：', users[0], 'provincename：', users[1])

            #gj = input("请输入你要查看最新新闻的疫情国家：")
            gj =users[1]
            cj =users[0]
            self.GJ = gj+"新型肺炎最新动态"
            # 构造url
            url = self.load_url.format(self.GJ)
            # 发生请求
            data = self.send_request(url)
            # 解析数据
            self.parse_jsondata(data,gj)
            # 显示数据
            self.show_data(gj,cj)
        cur.close()
        conn.close()
        print("*"*125)

print("*"*125)
print("*"+" "*50+"欢迎使用疫情新闻查询系统"+" "*50+"*")

yq().run()