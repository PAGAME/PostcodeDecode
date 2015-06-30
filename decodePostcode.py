#!/usr/bin/env python
# encoding: utf-8

import jieba
import jieba.posseg

def decodePostcode(strs):
    words = jieba.posseg.cut(strs)
    dictW = {'1' : '',
             '2' : '',
             '3' : ''}
    i = 1
    for word, flag in words:
        if flag == 'ns':
            print word
            dictW['%d'%i] = word
    print dictW
# strs = "北京刷卡缴费记录大妇科技术的垃圾发电是"
# decodePostcode(strs.decode('utf-8'))
