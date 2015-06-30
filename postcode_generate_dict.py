#!/usr/bin/env python
# encoding: utf-8

import re

def generate_dict():
    '''将config文件读取，并生成一个dict'''
    file_obj = open('postcode_conf')
    Dict = {
            }
    pattern = re.compile('([0-9]+)')
    for line in file_obj:
        list = re.split(pattern, line)
        print list
        list.remove('\n')
        i = 0
        print len(list)
        while i<len(list):
            Dict["%s"%(list[i])] = str(list[i+1])
            print Dict["%s"%(list[i])]
            i = i + 2
        print line
    return Dict
    
if __name__ == "__main__":
    dict = generate_dict()
    print dict