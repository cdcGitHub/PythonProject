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
from PIL import Image, ImageEnhance,ImageFilter
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
    
    im = ImageEnhance.Sharpness(im).enhance(2)
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(5)
    im = im.convert("1")
    im = im.filter(ImageFilter.ModeFilter(2))
    
    final_pic = im
    final_pic.show()
    strabc = pytesseract.image_to_string(final_pic)
    print(strabc)

'''    
    im = Image.open("pic.jpg")
    im.show()
    im = ImageEnhance.Sharpness(im).enhance(3)
    im.show()
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(3)
    im.show()
    im = im.convert("1")
    im.show()   
    final_pic = im
''' 
