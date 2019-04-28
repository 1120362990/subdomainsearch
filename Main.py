# -*- coding: utf-8 -*-
import os
from domains_scan.domain_scan_main import Domains_Scan


class Program(object):
    def __init__(self, url):
        self.path = (os.path.dirname(os.path.realpath(__file__)))
        self.url = url
        self.domains = Domains_Scan(self.url)
        # print(self.url)


if __name__ == "__main__":
    Program('feei.cn')  # thanks for feei.com  :)
