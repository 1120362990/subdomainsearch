# -*- coding: utf-8 -*-
import socket
import os


class Domain_Verified(object):
    def __init__(self, domains,path):
        self.domains = domains
        self.path = path

        def verified():
            os.chdir(self.path)
            domains = list(set(self.domains))
            for domain in domains:
                try:
                    print(domain, socket.gethostbyname(domain))
                    with open('domains_result.txt', 'a') as out_file:
                        out_file.write(domain+' '+socket.gethostbyname(domain) + '\n')
                    with open('IP_result_tem.txt', 'a') as out_file:
                        out_file.write(socket.gethostbyname(domain) + '\n')
                except Exception:
                    pass

        verified()
        
        #  Duplicate removal
        outfile = open('IP_result.txt', 'w')
        list_1 = []
        for line in open('IP_result_tem.txt'):
            tmp = line.strip()
            if tmp not in list_1:
                list_1.append(tmp)
                outfile.write(line)
        outfile.close()
        os.remove('IP_result_tem.txt')

    

        # get numbers
        count = 0
        thefile = open("domains_result.txt", "r")
        while True:
            buffer = thefile.read(1024*8192)
            if not buffer:
                break
            count += buffer.count('\n')
        thefile.close()
        print('[+]Domains total found:', count)
