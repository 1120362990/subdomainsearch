# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from requests.packages import urllib3
import threading,sys
import queue

def subdomainsearch_crt(domain):
    print('crt start')
    #第一次请求
    urllib3.disable_warnings()#消除证书认证告警
    url = r'https://crt.sh/?Identity=%25%25.'+domain
    re = requests.get(url=url, verify=False)
    soup = BeautifulSoup(re.content,"lxml")
    finds = [] #找到的域名存放区，用来检测去重
    cts = [] # 将得到的有*号的域名# 类似 *.baidu.com  的域名留存，为后续进行查找做准备
    cts1 = [] #用来存储已经检测过的带*的域名
    op = open('crt_jieguo.txt',"w+",encoding='utf-8')
    for num in range(3,len(soup.find_all('tr'))):
        # print(soup.find_all('tr')[num].find_all('td')[4].get_text().strip())
        if soup.find_all('tr')[num].find_all('td')[4].get_text().strip()[:1] == '*':
            if soup.find_all('tr')[num].find_all('td')[4].get_text().strip() not in cts:
                cts.append(soup.find_all('tr')[num].find_all('td')[4].get_text().strip()) # 存在*号的域名添加进列表中
        else:
            if soup.find_all('tr')[num].find_all('td')[4].get_text().strip() not in finds:
                op.write(soup.find_all('tr')[num].find_all('td')[4].get_text().strip()+'\n')  #正常的域名写入条形图中
                finds.append(soup.find_all('tr')[num].find_all('td')[4].get_text().strip())
    #针对第一次请求中发现的带有*的域名进行二次查询。bs4感官上非常慢，这里之后可以写成多线程
    for ct in cts:
        url = r'https://crt.sh/?Identity=%25%25.' +ct[2:]
        re = requests.get(url=url, verify=False)
        soup = BeautifulSoup(re.content, "lxml")
        for num in range(3, len(soup.find_all('tr'))):
            if soup.find_all('tr')[num].find_all('td')[4].get_text().strip()[:1] == '*':
                if soup.find_all('tr')[num].find_all('td')[4].get_text().strip() in cts or soup.find_all('tr')[num].find_all('td')[4].get_text().strip() in cts1:
                    pass#将已检测过的带*的域名剔除检测范围
                else:
                    cts.append(soup.find_all('tr')[num].find_all('td')[4].get_text().strip())#增添新发现的带*的域名
            else:
                if soup.find_all('tr')[num].find_all('td')[4].get_text().strip() not in finds:
                    op.write(soup.find_all('tr')[num].find_all('td')[4].get_text().strip() + '\n')  # 正常的域名写入条形图中
                    finds.append(soup.find_all('tr')[num].find_all('td')[4].get_text().strip())
        cts1.append(cts[0])
        cts.pop(0)
        print(cts)
        print(finds)

    op.close()

if __name__ == "__main__":
    subdomainsearch_crt()