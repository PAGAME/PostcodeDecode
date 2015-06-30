# -*- encoding:UTF8 -*-

import re
import httpclient
http = httpclient.Http()

class Zipcode:
    def __call__(self,area):

        url = "http://opendata.baidu.com/post/s?wd=%s&p=mini&rn=20"%http.quote(area.encode("gbk"))
        html = http.connect(url,encoding="gbk")
        if u"抱歉，没有找到" in html:
            error = u"抱歉，没有找到与“%s”相关的邮政编码信息，请重新输入关键词查询。"%area
            return error

        if area.isdigit():
            result_html = http.get_tag_html(html,"article",{"class":"region-data"})
        else:    
            result_html = http.get_tag_html(html,"article",{"class":"list-data"})
            if not result_html:
                result_html = http.get_tag_html(html,"article",{"class":"table-data"})
                

        print result_html
        result = http.html2txt(result_html[0])
        return result

class Decode():
    def __init__(self, strs):
        self.strs = strs

    def decodePostcode(self):
        parttern1 = re.compile('北京')
        parttern2 = re.compile('上海')
        while True:
            match = parttern1.match(strs)
            if match:
                print match.group()
                return match.group()

if __name__ == "__main__":

    test = Zipcode()
    print test(u"贵州")
    print type(test(u"云南"))
