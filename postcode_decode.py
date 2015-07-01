#!/usr/bin/env python
# encoding: utf-8

import jieba
import jieba.posseg
import postcode_generate_dict

def decodePostcode(strs):
    '''我们在这里假设，大家都习惯将大的地域写在地址的前面 eg:不会写 XXX单元 XXX小区 垂柳街 北京市
    返回一个包含字符串 K-V为 地点-邮编 的字典'''
    words = jieba.posseg.cut(strs)
    dictW = {}
    i = 1
    for word, flag in words:
        if flag == 'ns':
            print word
            dictW['code%d'%i] = word
            i = i + 1
    postcodeDict = getDict_and_compare(dictW)
    print dictW
    return postcodeDict

def getDict_and_compare(dict_NS):
    dictG = postcode_generate_dict.generate_dict()
    postcodeDict = {}
    print dictG
    for (a, b) in dict_NS.items():
        print a, b
        if b.encode('utf-8') in dictG:
            postcodeDict["%s"%(b.encode('utf-8'))] = dictG[b.encode('utf-8')]
            print dictG[b.encode('utf-8')]
            print '查找地区邮编成功'
        else:
            print "没有查找到相应的邮编"
    return postcodeDict

if __name__ =="__main__":
    strs = "北京市刷卡缴费朝阳区记录妇科技术的垃圾发电是"
    decodePostcode(strs.decode('utf-8'))
