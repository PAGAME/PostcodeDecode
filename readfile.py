#!/usr/bin/env python
# encoding: utf-8
import re
import jieba
import jieba.posseg as pseg

file_object = open('postcode_conf')
output = open('end.py', 'w')

pattern = re.compile('([^0-9]+)([0-9]+)([^0-9]+)([0-9]+)([^0-9]+)([0-9]+)([^0-9]+)([0-9]+)')
pattern2 = re.compile('.+')
# patternxx=re.compile(u"([/u4e00-/u9fa5]+)") 

try:
    for line in file_object:
        uline = line.decode('utf-8')
        match = re.match(pattern, line)
        if match:
            print match.group(0)
            words = pseg.cut(match.group(0))
            for word, flag in words:
                print("%s %s" %(word,flag))
#         if match:
#             i = 0
#             seg_list = jieba.cut(match.group(i))
#             print ("/".join(seg_list))
#             while i < 8:
#                 output.write(match.group(i) + ':')
#                 print match.group(i)
#                 i = i+1
#         else:
#              print"  _____"
finally:
     file_object.close()
