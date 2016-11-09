# -*- coding: utf-8 -*-
"""

Created on Tue Nov  1 09:25:11 2016
调度器，负责调用页面下载，页面解析对象和json写入对象

"""

import html_downloader
import html_parser
import json_outputer

import time
import random

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = json_outputer.JsonOutputer()

    def spider(self,root_url):
#        print "Spider opened!"

        #下载根页面，并解析获得每个类别的url
        cats_cont = self.downloader.download(root_url)
        cats_urls = self.parser.parse_cats_urls(cats_cont)
        cat_count=0    
        count = 0
        for cat_url in cats_urls:  #对类别进行遍历

#            cat_url=cats_urls[cat_count]
            print("Start Crawing category %s" % cat_url)
            try: 
                pages_cont = self.downloader.download(cat_url)  #下载类别的第一页

                pages_urls = self.parser.parse_pages_urls(pages_cont,cat_url)#解析，获得每一页的链接，返回到数组pages_urls
#               print(pages_urls)            
                for page_url in pages_urls:
                    print("Start Crawing page %s." % page_url)
                try:
                    booklist_cont = self.downloader.download(page_url)#下载图书列表页面
#                   print(booklist_cont.read())
                    booklist_urls = self.parser.parse_book_urls(booklist_cont)#解析，获得该页每本书的链接，返回到数组
#                   print(booklist_urls)

#                    try:
                    for book_url in booklist_urls:
                        book_cont = self.downloader.download(book_url)#下载图书内容的页面
                    
                        book_detail = self.parser.parse_book_details(book_cont)#解析，获得图书的各项信息
                        #                    print(book_detail)
                        self.outputer.collect_data(book_detail)#把图书基本信息存储到对象中
                        time.sleep(random.randint(2,5))#随机停止数秒，避免操作过于频繁
                        count += 1
                    print("Crawed book %s successfully!" % book_detail['title'])
#                    except:
#                            print("Craw Failed for app %s." % book_url)
                except:
                    print("Craw Failed for page %s." % page_url)

                print("Totally Crawed %d books now." % count)


                self.outputer.output_json(str(cat_count)+".json")#写入数据到json文件
                cat_count=cat_count+1
#                
#                name = 'category' + re.findall(r'\d+',cat_url)[0] + ".json"
#                self.outputer.output_json(name)
            except:
                print("Craw failed for category %s !" % cat_url)
 




if __name__ == "__main__":
    root_url = 'https://read.douban.com/ebooks/'
    spider = SpiderMain()
    spider.spider(root_url)