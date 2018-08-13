import requests,time,random,re,json,functools
from multiprocessing import Pool,Manager


header=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]
def get_one_page(url):
    headers={
        "User-Agent":random.choice(header)
    }
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text

        return None
    except ReqestException:
        return None

def deal_one_page(html):
    pattern=re.compile('<p class="name">[\s\S]*?title="([\s\S]*?)"[\s\S]*?'
                       '<p class="star">([\s\S]*?)</p>[\s\S]*?'
                       '<p class="releasetime">([\s\S]*?)</p>[\s\S]*?')
    results=re.findall(pattern,html)
    for item in results:
        yield {
            "电影名称:":item[0].strip(),
            "主演:":item[1].strip(),
            "上映时间:":item[2].strip()
            }
def write2File(item):
    with open('maoyan_yeild.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False)+'\n')

def crawlPage(lock,Num):
    url="http://maoyan.com/board/6?offset={}".format(Num)
    html=get_one_page(url)
    for item in deal_one_page(html):
        lock.acquire()
        write2File(item)
        lock.release()

if __name__=="__main__":
    # for x in range(0,100,10):
    #     crawlPage(x)
    #
    #     time.sleep(random.randint(1,3))
    manager=Manager()
    lock=manager.Lock()

    pcrawlpage=functools.partial(crawlPage,lock)
    pool=Pool()
    pool.map(pcrawlpage,[i*10 for i in range(10)])
    pool.close()
    pool.join()

    print('Finished')