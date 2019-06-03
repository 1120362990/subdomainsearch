# -*- coding: utf-8 -*-
import requests
import re
from requests.packages import urllib3
import time
from bs4 import BeautifulSoup


class Web_Domain_Search(object):
    def __init__(self, url):
        self.url = url
        # self.result

        def subdomainsearch_baidu(domain):
            print('[+]Baidu search domains start!', time.asctime(time.localtime(time.time())))
            domains_baidu = []

            def danyedayin(zhuyuming, changdu):  # 百度搜索出的单页结果打印
                url = 'http://www.baidu.com/s?wd=site:'+zhuyuming+'&pn='+changdu
                try:
                    urllib3.disable_warnings()  # 消除证书认证告警
                    response = requests.get(url, verify=False, timeout=5).content.decode('utf-8')
                    subdomain = re.findall('style="text-decoration:none;">(.*?)/', response)
                    i = 0
                    while i < len(subdomain):
                        domains_baidu.append(subdomain[i])
                        i = i + 1
                    return
                except Exception:
                    pass
            # 主流程
            o = 0
            while o < 100:  # set page numbers . there is 100
                print(o ,'/100')
                changdu = str(o*10)
                danyedayin(domain, changdu)
                o = o + 1
            print('[-]Baidu search domains is done!', time.asctime(time.localtime(time.time())))
            # print('baidu',domains_baidu)
            return(domains_baidu)

        def subdomainsearch_crt(domain):
            print('[+]Crt search domains start!', time.asctime(time.localtime(time.time())))
            # 第一次请求
            urllib3.disable_warnings()#消除证书认证告警
            url = r'https://crt.sh/?Identity=%25%25.'+domain
            re = requests.get(url=url, verify=False)
            soup = BeautifulSoup(re.content, "lxml")
            domains_crt = []  # 找到的域名存放区，用来检测去重
            for num in range(3, len(soup.find_all('tr'))):
                domains_crt.append(soup.find_all('tr')[num].find_all('td')[4].get_text().strip())
            print('[-]Crt search domains is done!', time.asctime(time.localtime(time.time())))
            # print('crt',domains_crt)
            return(domains_crt)


        #  deal , threading
        domains = []
        technology  = []

        try:
            a = subdomainsearch_baidu(self.url)
            technology .append(a)
        except Exception:
            print('[-]Baidu error!')
            pass
        try:
            b = subdomainsearch_crt(self.url)
            technology .append(b)
        except Exception:
            print('[-]CRT error!')
            pass


        # technology = [subdomainsearch_baidu(self.url),subdomainsearch_crt(self.url)]
        for x in technology:
            for y in x:
                domains.append(y)
        print('[-]Domains search is done! Found', len(domains), '!', time.asctime(time.localtime(time.time())))
        self.result = domains
