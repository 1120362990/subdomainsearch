# -*- coding: utf-8 -*-
from requests.packages import urllib3
import requests
import re
import os
from urllib.parse import urlparse

def subdomainsearch_360(domain):
    def danyedayin(zhuyuming,changdu):#搜索出的单页结果打印
        url='http://www.so.com/s?q=site:'+zhuyuming+'&pn='+changdu
        try:
            urllib3.disable_warnings()#消除证书认证告警
            response=requests.get(url,verify=False,timeout=5).content.decode('utf-8')
            subdomain=re.findall('<cite>(.*?)</cite>',response)
            i = 0
            while i < len(subdomain):
                fo.write(re.findall('[a-zA-Z\.0-9]+(?=\/)',subdomain[i])[0]+"\n")
                i = i + 1
            return
        except:
            pass
    def wnjianqucong():#文件去重
        outfile = open('360_jiguoIP.txt', 'w') #新的文件
        list_1=[]
        for line in open('360_foo.txt'):  #老文件
            tmp = line.strip()
            if tmp not in list_1:
                list_1.append(tmp)
                outfile.write(line)
        outfile.close()
    def wnjianhangshu():#获取收集的IP个数
        filename = "360_jiguoIP.txt"
        myfile = open(filename)
        lines = len(myfile.readlines())
        myfile.close()
        print("360 total found  %s IPS." % (lines))
    #360域名匹配的特殊处理，给域名后面加上  .com
    def jiacom():
        f = open("360_jiguoIP.txt", "r")
        fopen = open("360_jieguo.txt", "w")
        while True:
            line = f.readline()
            if line:
                line=line.strip()
                p = line +'.com'+ "\n"
                fopen.write( p )
            else:
                break
        fopen.close()

    #以下为扫描的主流程，包含一些默认配置
    zhuyuming = domain
    shoujigshu = 64
    fo = open("360_foo.txt","a")
    o = 0
    while o < shoujigshu:
        changdu = str(o+1)
        danyedayin(zhuyuming,changdu)
        print(str(o)+' page. '+'Total '+str(shoujigshu)+' page.')
        o = o + 1
    fo.close()
    wnjianqucong()
    wnjianhangshu()
    os.remove('360_foo.txt')
    jiacom()
    os.remove('360_jiguoIP.txt')

if __name__ == "__main__":
    subdomainsearch_360()