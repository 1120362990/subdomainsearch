# -*- coding: utf-8 -*-
import requests
import re
import os
from requests.packages import urllib3

def subdomainsearch_baidu(domain):
    def danyedayin(zhuyuming,changdu):#百度搜索出的单页结果打印
        url='http://www.baidu.com/s?wd=site:'+zhuyuming+'&pn='+changdu
        try:
            urllib3.disable_warnings()#消除证书认证告警
            response=requests.get(url,verify=False,timeout=5).content.decode('utf-8')
            subdomain=re.findall('style="text-decoration:none;">(.*?)/',response)
            i = 0
            while i < len(subdomain):
                fo.write(subdomain[i]+"\n")
                i = i + 1
            return
        except:
            pass
    def wnjianqucong():#文件去重
        outfile = open('baidu_jiguoIP.txt', 'w') #新的文件
        list_1=[]
        for line in open('baidu_foo.txt'):  #老文件
            tmp = line.strip()
            if tmp not in list_1:
                list_1.append(tmp)
                outfile.write(line)
        outfile.close()
    def wnjianhangshu():#获取收集的IP个数
        filename = "baidu_jiguoIP.txt"
        myfile = open(filename)
        lines = len(myfile.readlines())
        myfile.close()
        print("Total found  %s IPS." % (lines))
    #主流程
    zhuyuming = domain
    shoujigshu = 100
    fo = open("baidu_foo.txt","a")
    o = 0
    while o < shoujigshu:
        changdu = str(o*10)
        danyedayin(zhuyuming,changdu)
        print(str(o)+' page. '+'Total '+str(shoujigshu)+' page.')
        o = o + 1
    fo.close()
    wnjianqucong()
    wnjianhangshu()
    os.remove('baidu_foo.txt')


if __name__ == "__main__":
    subdomainsearch_baidu()