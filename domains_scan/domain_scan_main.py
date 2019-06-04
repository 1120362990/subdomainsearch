# -*- coding: utf-8 -*-
from ESD import EnumSubDomain
from .web_domain_search import Web_Domain_Search
import os


class Domains_Scan(object):
    def __init__(self, url, path):
        self.url = url
        self.path = path

        # start ESD   exception handling?
        def esd_search():
            try:
                Esddomains = []
                for key in EnumSubDomain(self.url).run():
                    Esddomains.append(key)
                self.url1 = Esddomains
            except Exception:
                print('ESD error!')

        # start web_domains_search
        def web_search():
            try:
                Web_domains = Web_Domain_Search(self.url)
                self.url2 = Web_domains.result
            except Exception:
                print('Web_Domain_Search error!')

        # start subDomainsBrute_domain_search
        def subDomainsBrute_search():
            try:
                os.chdir(self.path+'/domains_scan/subDomainsBrute')
                os.system(f'python2.7  subDomainsBrute.py {self.url}')
                try:
                    subDomainsBrute_urls = []
                    with open(f'{self.url}.txt', 'r', encoding  = 'utf-8') as f:
                        for line in f:
                            subDomainsBrute_urls.append(line.strip().split(' ')[0])
                    os.system(f'rm -rf {self.url}.txt')
                    self.url3 = subDomainsBrute_urls
                except Exception:
                    self.url3 = []
                    pass
            except Exception:
                print('ubDomainsBrute_search error!')

        # start
        try:
            subDomainsBrute_search() # url3
        except Exception:
            print('[-]subDomainsBrute_search error!  url3')
            self.url3 = []
        try:
            esd_search()  # url1
        except Exception:
            self.url1 = []
            print('[-]esd_search error! url1')
        try:
            web_search()  # url2
        except Exception:
            self.url2 = []
            print('[-]web_seach error! url2')

        domains_all = []
        technology = [self.url1, self.url2, self.url3]
        for x in technology:
            for y in x:
                domains_all.append(y)

        self.domains = domains_all
