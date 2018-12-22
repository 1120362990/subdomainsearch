# -*- coding: utf-8 -*-
import requests
import re
import os
from requests.packages import urllib3

def subdomainsearch_bing_guonei(domain):
    def danyedayin(zhuyuming,changdu):#百度搜索出的单页结果打印
        url='http://cn.bing.com/search?q=site:'+zhuyuming+r'&go=%E6%90%9C%E7%B4%A2&first='+changdu
        try:
            urllib3.disable_warnings()#消除证书认证告警
            response=requests.get(url,verify=False,timeout=5).content.decode('utf-8')
            subdomain=re.findall('target="_blank" href="https://(.*?)/',response)
            i = 0
            while i < len(subdomain):
                #print subdomain[i]
                fo.write(subdomain[i]+"\n")
                i = i + 1
            return
        except:
            pass
    def wnjianqucong():#文件去重
        outfile = open('bing_guonei_jiguoIP.txt', 'w') #新的文件
        list_1=[]
        for line in open('bing_guonei_foo.txt'):  #老文件
            tmp = line.strip()
            if tmp not in list_1:
                list_1.append(tmp)
                outfile.write(line)
        outfile.close()
    def wnjianhangshu():#获取收集的IP个数
        filename = "bing_guonei_jiguoIP.txt"
        myfile = open(filename)
        lines = len(myfile.readlines())
        myfile.close()
        print("Total found  %s IPS." % (lines))
    #主要
    zhuyuming = domain
    shoujigshu = 50
    fo = open("bing_guonei_foo.txt","a")
    o = 0
    while o < shoujigshu:
        changdu = str(o+10)
        danyedayin(zhuyuming,changdu)
        print(str(o)+' page. '+'Total '+str(shoujigshu)+' page.')
        o = o + 1
    fo.close()
    wnjianqucong()
    wnjianhangshu()
    os.remove('bing_guonei_foo.txt')

if __name__ == "__main__":
    subdomainsearch_bing_guonei()
