# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from requests.packages import urllib3

def subdomainsearch_crt(domain):
    print('crt start')
    #第一次请求
    urllib3.disable_warnings()#消除证书认证告警
    url = r'https://crt.sh/?Identity=%25%25.'+domain
    re = requests.get(url=url, verify=False)
    soup = BeautifulSoup(re.content,"lxml")
    finds = [] #找到的域名存放区，用来检测去重
    op = open('crt_jieguo.txt',"w+",encoding='utf-8')
    for num in range(3,len(soup.find_all('tr'))):
        print(num,len(soup.find_all('tr')),soup.find_all('tr')[num].find_all('td')[4].get_text().strip())
        if soup.find_all('tr')[num].find_all('td')[4].get_text().strip()[:1] == '*':
            if soup.find_all('tr')[num].find_all('td')[4].get_text().strip()[2:] not in finds:
                op.write(soup.find_all('tr')[num].find_all('td')[4].get_text().strip()[2:]+'\n')# 存在*号的域名,将*去掉后写入txt
                finds.append(soup.find_all('tr')[num].find_all('td')[4].get_text().strip()[2:])
        else:
            if soup.find_all('tr')[num].find_all('td')[4].get_text().strip() not in finds:
                op.write(soup.find_all('tr')[num].find_all('td')[4].get_text().strip()+'\n')  #正常的域名写入到txt中
                finds.append(soup.find_all('tr')[num].find_all('td')[4].get_text().strip())
    op.close()
    print('crt all done')

if __name__ == "__main__":
    subdomainsearch_crt()