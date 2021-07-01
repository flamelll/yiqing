# -*- codeing = utf-8 -*-
# @Time : 2020/3/3 17:51
# @Author : 李巍
# @File : spider.py
# @Software: PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
    # 1.爬取网页
    datalist = getData(baseurl)
    # savepath = "豆瓣电影Top250.xls"
    dbpath = "bobao.db"
    # 3.保存数据
    # saveData(datalist,savepath)
    saveData2DB(datalist, dbpath)

    askURL("https://ncov.dxy.cn/ncovh5/view/pneumonia")


# 影片详情链接的规则
findLink = re.compile(r'<p class="topicTitle___2ovVO">')  # 创建正则表达式对象，表示规则（字符串的模式）


# 爬取网页
def getData(baseurl):
    datalist = []

    url = baseurl + str(5)
    html = askURL(url)  # 保存获取到的网页源码

    # 2.逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表

     data = []  # 保存一部电影的所有信息
     item = str(item)

        # 影片详情的链接
     link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串
     data.append(link)  # 添加链接



     datalist.append(data)  # 把处理好的一部电影信息放入datalist

    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(datalist, savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('bobao', cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接")

    sheet.write(0, 1, col[0])  # 列名
    for i in range(0, 5):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 5):
            sheet.write(i + 1, j, data[j])  # 数据

    book.save(savepath)  # 保存


def saveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
                insert into bobao (
                info_link) 
                values(%s)''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table bobao 
        (
        id integer primary key autoincrement,
        info_link text
        )

    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    # init_db("movietest.db")
    print("爬取完毕！")