# -*- coding: utf-8 -*-
import os
from domains_scan.domain_scan_main import Domains_Scan
from domain_verified.domain_verified_main import Domain_Verified
from optparse import OptionParser
import sys

class Program(object):
    def __init__(self, url):
        self.path = (os.path.dirname(os.path.realpath(__file__)))
        self.url = url
        self.domains = Domains_Scan(self.url, self.path).domains
        Domain_Verified(self.domains, self.path)


if __name__ == "__main__":

    usage = "M.py  xxxx.com "
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.print_help()
        sys.exit()

    Program(args[0])
