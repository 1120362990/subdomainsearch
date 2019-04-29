# -*- coding: utf-8 -*-
from ESD import EnumSubDomain
from .web_domain_search import Web_Domain_Search


class Domains_Scan(object):
    def __init__(self, url):
        self.url = url

        # start ESD   exception handling?
        def esd_search():
            try:
                esddomains = EnumSubDomain(self.url).run()
                print(esddomains)
            except Exception:
                print('ESD error!')
        # esd_search()

        # start web_domains_search
        try:
            Web_Domain_Search(self.url)
        except Exception:
            print('Web_Domain_Search error!')
        
