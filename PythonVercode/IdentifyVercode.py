#coding=utf-8
import requests
import json
import sys
import os
import urllib
import re
#from lxml import etree
#from multiprocessing.dummy import Pool as ThreadPool
import time
from PIL import Image
import PIL.ImageOps
from pytesseract import *
#reload(sys)
#sys.setdefaultencoding('utf-8')
#type = sys.getfilesystemencoding()
# hea = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
url = "http://hd.hinews.cn/2/checkcode.php"
for i in range(1,5):
    html = requests.get(url, headers=hea, timeout=60).content
    fp = open("pic.jpg", 'wb')
    fp.write(html)
    fp.close()

    im = Image.open("pic.jpg")
    im.show()
    im = im.convert('L')
    def initTable(threshold = 200):
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return table

    binaryImage = im.point(initTable(),'1')
    im1 = binaryImage.convert('L')

    final_pic = im
    
    final_pic.show()
    strabc = pytesseract.image_to_string(final_pic)
    print(strabc)
'''
class spiderIt:
    root_url = 'http://r2.1024cls.club/pw/thread.php?fid=14&page='


    def get_all_page_url(self, num_min, num_max):
        all_page_url = []
        for i in range(num_min, num_max+1):
            all_page_url.append("%s%s"%(self.root_url, i))
        return all_page_url

    def get_html_of_one_page(self, page_url):
        html = requests.get(page_url, headers=hea, timeout=60)
        html.encoding = 'utf-8'
        return html.text

    def get_all_pic_page_url_in_one_page(self, page_url):
        html = self.get_html_of_one_page(page_url)
        selector = etree.HTML(html)
        groupLinkIncomplete = selector.xpath('//*[starts-with(@id, "td_")]/h3/a/@href')
        groupLink = []
        for i in range(0,len(groupLinkIncomplete), 1):
                completeLink = re.sub('thread.php\?fid=14&page=\d+', groupLinkIncomplete[i], page_url, re.S)
                groupLink.append(completeLink)
        return groupLink

    def get_all_pic_link_in_one_pic_page(self, pic_page_url):
        pic_html = self.get_html_of_one_page(pic_page_url)
        selector = etree.HTML(pic_html)
        pic_link = selector.xpath('//*[@id="read_tpc"]/img/@src')
        return pic_link

    def get_all_pic_name_in_one_pic_page(self, pic_page_url):
        pic_html = self.get_html_of_one_page(pic_page_url)
        selector = etree.HTML(pic_html)
        pic_name = selector.xpath('//*[@id="subject_tpc"]/text()')[0]
        return pic_name

    def download_one_pic(self, pic_pathname_link):
        save_path_name = pic_pathname_link[0]
        pic_url = pic_pathname_link[1]
        # print save_path_name + ':' + pic_url
        # print  pic_url
        download_count = 0
        pic_content = 0
        while download_count < 5:
            try:
                pic_content = requests.get(pic_url, headers=hea, timeout=10).content
                break
            except Exception, e:
                download_count += 1

        if download_count == 5:
            fp = open("log.txt", "w+")
            fp.write("%s : %s download failed!"%(save_path_name, pic_url))
            fp.close()
        else:
            try:
                fp = open(save_path_name, 'wb')
                fp.write(pic_content)
                fp.close()
            except Exception, e:
                fp = open("log.txt", "w+")
                fp.write("%s : %s save failed!" % (save_path_name, pic_url))
                fp.close()


test = spiderIt()
try:
    os.mkdir("E:\\download")
    print "E:\\download dir has been created"
except Exception, e:
    print "E:\\download dir has been created before!"

test_url = test.get_all_page_url(2,10)
print "Big Page Get",
print test_url

for each in test_url:
    try:
        test_pic_page_url = test.get_all_pic_page_url_in_one_page(each)
    except Exception, e:
        continue

    print "Sub Page Get",
    print test_pic_page_url

    for each_pic_page_url in test_pic_page_url:
        try:
            all_pci_name = test.get_all_pic_name_in_one_pic_page(each_pic_page_url)
        except Exception, e:
            continue

        try:
            os.mkdir("E:\\download\\%s"%all_pci_name)
            print "E:\\download\\%s dir has been created"%all_pci_name
        except Exception, e:
            print "E:\\download\\%s dir has been created before! Jump over it"%all_pci_name
            continue

        all_pic_link = test.get_all_pic_link_in_one_pic_page(each_pic_page_url)
        print "Pic Link Get",
        print all_pic_link

        all_pic_pathname_link = []

        for each_pic_link in all_pic_link:
            temp = []

            try:
                single_pic_name = re.findall("http://.*/(.*?)\.jpg", each_pic_link)[0]
            except Exception, e:
                continue

            temp.append("E:\\download\\%s\\%s.jpg"%(all_pci_name, single_pic_name))

            temp.append(each_pic_link)

            all_pic_pathname_link.append(temp)


        pool = ThreadPool(8)
        time_start = time.time()
        result = pool.map(test.download_one_pic, all_pic_pathname_link)
        pool.close()
        pool.join()
        time_end = time.time()
        print "%s 8线程 共消耗："%each_pic_page_url + str(time_end-time_start)
'''
