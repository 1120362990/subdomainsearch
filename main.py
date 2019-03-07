# -*- coding: utf-8 -*-
import crt
import sanliuling
import baidu
import threading
import os

def subdomainsearch_main(domain):
    print('statrt')
    modules = [crt.subdomainsearch_crt,sanliuling.subdomainsearch_360,baidu.subdomainsearch_baidu]
    nmodules = range(len(modules))
    threads = []   #这个类似于一个线程池
    for module in modules:
        t = threading.Thread(target=module,args=(domain,))  #实例化thread类
        threads.append(t)   #添加线程
    for i in nmodules:
        threads[i].start()   #启动线程
    for i in nmodules:
        threads[i].join()   #阻塞，直到线程结束。守护进程不需要启用这一项

    domains = []
    txts = ['360_jieguo.txt','baidu_jiguoIP.txt','crt_jieguo.txt']
    for txt in txts:
        for lines in open(txt,"r"):
            if lines.strip() not in domains:
                if lines.strip() != 'https:':#这里需要处理一下，匹配出结果中的域名
                    domains.append(lines.strip())
        os.remove(txt)
    op = open('result.txt',"w+")
    for domain in domains:
        op.write(domain+'\n')
    op.close()
    print('all done')

if __name__ == "__main__":
    subdomainsearch_main('xxx.net')
