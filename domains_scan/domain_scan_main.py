# -*- coding: utf-8 -*-
from ESD import EnumSubDomain


class Domains_Scan(object):
    def __init__(self, url):
        self.url = url 
        print(self.url)

        # start ESD   exception handling?
        def esd_search():
            try:
                esddomains = EnumSubDomain(url).run()
                print(esddomains)
            except Exception:
                print('ESD error!')
        # esd_search()
