# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:40:45 2016

@author: Administrator
"""
from bs4 import BeautifulSoup
import re

url_root='https://read.douban.com/ebooks/'
class HtmlParser(object):
    
    def parse_cats_urls(self,response):
        
        soup = BeautifulSoup(response.read().decode('utf-8'),'html.parser')
        urls = []
        for child in soup.findAll("ul",{"class":"categories-list"})[0].children:
            urls.append("https://read.douban.com"+child.a['href'])#获取每一类别的链接
        return urls

#某一类别下，每一页的链接
    def parse_pages_urls(self,response,url):
        soup = BeautifulSoup(response.read().decode('utf-8'),'html.parser')
        last_page=soup.find("li",{"class":"next"}).previous_sibling #找到最后一页的页码
        if last_page:    
            pages=int(last_page.text)
        urls=[]
        for i in range(pages):  
            urls.append(url+'?cat=book&sort=top&start='+str(i*20))     

        return urls        

#某一页中，每本书的链接
    def parse_book_urls(self,response):
        soup = BeautifulSoup(response.read().decode('utf-8'),'html.parser')
#        print(soup)
        urls=[]
        for content in soup.select('.info'): 
#            print(content)
            link=str(content.select('.title')[0].select("a[href]"))
            r=re.compile(r'/ebook/[0-9]+/')
            book_id=r.findall(link)[0][7:-1]
            href='https://read.douban.com/ebook/'+str(book_id)+'/'
            urls.append(href)

        return urls


#获取图书基本信息
    def parse_book_details(self,response):
        soup = BeautifulSoup(response.read().decode('utf-8'),'html.parser')

        item={}
        list_contents=[]        
        
        bookurl=str(response.url)
        item["book_id"]=bookurl[bookurl.index("ebook/")+6:-1]
        
        
        item["url"]=bookurl
        
        item["title"]= soup.select('.article-title')[0].text #


        item["author"]='N' if len(soup.select('.author-item'))==0 else soup.select('.author-item')[0].text
        


        item["price"] ='0' if len(soup.select('.current-price-count'))==0 else soup.select('.current-price-count')[0].text[1:]
      
        item["category"] ='N' if len(soup.select('.category'))==0 else soup.select('.category')[0].text[3:]
        
        item["score"] ='0' if len(soup.select('.score'))==0 else soup.select('.score')[0].text

        item["eveluate_nums"]='0' if len(soup.select('.amount'))==0 else soup.select('.amount')[0].text[3:-4]

        item["desc"] ='N' if len(soup.select('.category'))==0 else soup.select('.info')[0].text
      
        item["publisher"]='N' if len(soup.select('.name'))<=1 else soup.select('.name')[1].text
#        item["raw_table_con"]=soup.select('.table-of-contents')[0]

#找到最深一层目录，'.level-0'，'.level-1'，'.level-2'都有可能，找到存在的数字最大的标签
        deep_level='.level-0'
        if len(soup.select('.level-1'))>0:
            deep_level='.level-1'
        if len(soup.select('.level-2'))>0:
            deep_level='.level-2'
            
            
#把'第*章*'等文字去掉，后来发现类似的文字很多种，应该在数据分析时再用正则表达式统一处理
        for line in soup.select(deep_level):
            r1=re.compile(r'^第.*章') #用'第*章*',’第*.章‘
            r2=re.compile(r'^\d\s')
            txt_chapter=r1.findall(line.text)
            txt_section=r2.findall(line.text)
#            print(txt_section)
            if len(txt_chapter)>0:
                list_contents.append(line.text[len(txt_chapter[0]):])
            elif len(txt_section)>0:
                list_contents.append(line.text[len(txt_section[0]):])
            else:
                list_contents.append(line.text)
            
            
        item["table_contents"]=list_contents
            
        tags=[]#获取图书的标签
        for tag in soup.find_all('span',{"class":"tag-name"}):
            tags.append(tag.text)        
        item["tags"]=tags


        # return dict for dumping into json file
        return item




