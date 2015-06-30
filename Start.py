#!/usr/bin/env python
# encoding: utf-8

def start(params):
    decode_province()
    decode_city()
    decode_country()
    return params

def decode_province():
    pass

def decode_city():
    pass

def decode_country():
    pass
if __name__ == "__main__":
    params = raw_input("please input:")
    print start(params)