# -*- coding:utf-8 -*-
'''
@project=爬虫
@file=MoiveInfo
@Author=Administrator
@creat_time=2018/8/1516:26
'''
import basicSpider

url="https://www.douban.com/doulist/114465/?start=0"

if __name__=="__main__":


    #抓取这页的数据
    html=CrawlInfo(seed_url)

    pattern='<a href="([\s\S]*?)&amp;sort=seq&amp;sub_type=">'

    itemurls=re.findall(pattern,html)

    #用队列与模拟广度优先遍历
    crawled_queue=[] #记录已爬url的队列
    crawl_queue=[]
    for itemurl in itemurls:
        #第一步去重,通过已爬队列来放置重复
        if itemurl not in crawled_queue:
            crawl_queue.append(itemurl)
        #第二部去重,保证待爬队列本身不重复
        crawl_queue=list(set(crawl_queue))

