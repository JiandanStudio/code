import time
import requests
from lxml import etree
from multiprocessing.dummy import Pool
from requests.exceptions import RequestException
import openpyxl
from fake_useragent import UserAgent
import os

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')
DesktopPath = GetDesktopPath()+'\\'
os.makedirs(DesktopPath+'新闻')#自己电脑的路径

def get_one_page(url):
    try:
        res = requests.get(url,headers = headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    # 构造HTML解析器
    h3_list  = html.xpath('//div[@class="text"]/h3')
    ul_list = html.xpath('//div[@class="text"]/ul')
    return h3_list,ul_list

def saveTxt(h3_list,ul_list,offset):
    
    filename  = '7月'+str(offset)+'日.txt'
    
    with open(DesktopPath+'新闻'+'\\'+filename,'a',encoding='utf-8') as f:
    # 写入
        for index,h3 in enumerate(h3_list):
            try:
                edition = h3.xpath('./text()')[0].strip()
                # print(edition)
                f.write(edition)
                f.write('\r\n')
                li_list = ul_list[index].xpath('./li')
                for li in li_list:
                    # print(li)
                    title = li.xpath('./a/text()')[0].strip()
                    link = 'http://paper.cnii.com.cn'+li.xpath('./a/@href')[0].strip()
                    # print(title)
                    # print(link)
                    f.write('标题：')
                    f.write(title)
                    f.write('\n')
                    f.write('链接')
                    f.write(link)
                    f.write('\n')
                    
                    # 获取二级页面（标题、日期、内容）
                    # time.sleep(2)
                    res1 = requests.get(link,headers = headers)
                    html_a = res1.text
                    html_a = etree.HTML(html_a)
                    title_container  = html_a.xpath('//div[@class="title-container"]')[0]
                    author = title_container.xpath('./span[@class="date"]/text()')[0].strip()
                    f.write('作者：')
                    f.write(author)
                    f.write('\t')
                    date = title_container.xpath('./p[@class="date"]/text()')[0].strip()
                    f.write('日期')
                    f.write(date)
                    f.write('\n')
                    content  = ''.join(html_a.xpath('//div[@class="text"]//text()'))
                    # 清洗
                    content  = content.replace('\n','').replace('\r','').replace(' ','').replace('\u3000','')
                    #print(content)
                    f.write('内容：')
                    f.write(content)
                    f.write('\n')
                    f.write('-'*50)
                    f.write('\n')
                f.write('='*150)
                f.write('\n')
            except Exception:
                pass
    f.close()

def main(offset):
    # 构造主函数，初始化各个模块，传入入口URL
    base_url = 'http://paper.cnii.com.cn/item/rmydb_2021_4_{}_1.html'
    url = base_url.format(offset)
    html = etree.HTML(get_one_page(url))
    h3_list,ul_list = parse_one_page(html)
    saveTxt(h3_list,ul_list,offset)




if __name__ == '__main__':
    # 请求头
    headers = {'User-Agent':UserAgent(verify_ssl=False).random}
    # 使用线程池
    print('多线程爬取开始')
    start_time=time.time()
    p = Pool(8)
    p.map(main,[i for i in range(12,14)])
    #关闭线程池
    end_time=time.time()
    print('多线程爬取结束')
    print('耗时:',end_time-start_time)
    p.close()
    p.join()#用来等待进程池中的worker进程执行完毕，防止主进程在worker进程结束前结束。
