# -*- coding: UTF-8 -*-
from sqlalchemy import false
from os import name
from bs4.dammit import chardet_type
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By
import re
import time
from bs4 import BeautifulSoup
import bs4
import lxml
import json
import base64
import random
from datetime import datetime
import code
from lxml import etree
import sys
from my_b import b_selenum as b
# sys.path.append("..") 
from my_location import *

# 点击，正常点击
def dj_sure(cx, path, path2,lx, name='',name2='',position1=0,position2=0):
    while True:
        if b.isElementExist(cx, path2, position=position2,name=name2):
            break
        else:
            # b.dj(cx, path, lx, name=name,position=position1)
            b.zxjs1(cx,path,position=position1)

# 获取文本，不报错
def hqwb_noerror(cx,path,position=0):
    try:
        t=cx.find_elements_by_xpath(
                f'{path}')[position].text
    except:
        t=''
    return t

# company 格式化
def company_format(company0,jg=' '):
    company=''
    for item in company0.split():
        if item != 'lnc' or item != 'LC':
            if company0.split().index(item) == 0:
                company = company + item
            else:
                company = company + jg + item
    return company

# 生成company_email
def make_company_email_hz(company0):
    company_email = ''
    for item in company0.split():
        if item != 'lnc' or item != 'LC':
            company_email = company_email + item
        company_email = company_email.replace(
            '\'', '').replace('&', '').replace('.', '')
    return company_email

# 获取搜索结果列表
def google_yz_yx(company_qx):
    site_l = []
    headers = {
        # 'Connection': 'keep-alive',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,la;q=0.6',
    }
    proxies = {"http": "http://127.0.0.1:30809",
               "https": "http://127.0.0.1:30809"}
    requests.adapters.DEFAULT_RETRIES = 3
    r = requests.get('https://www.google.com/search?q='+company_qx,
                     headers=headers, proxies=proxies)
    r.encoding = 'utf-8'
    text = r.text
    selector = etree.HTML(text)
    divs = selector.xpath('//div[@class="g"]/div/div/div/a')
    for item in divs:
        t = item.xpath('@href')[0]
        site_l.append(t)
    return site_l

# name 格式化
def name_gsh(name,index='',return_list=False):
    name_l = []
    x0 = name.split()[0].lower()
    x1 = name.split()[1].lower()
    if '.' in x1:
        x1 = x1.split('.')[0].lower()
        # 去掉空格 1
        name_l.append(x0+x1)
        if len(x1) !=1:
            name_l.append(x0+x1[0])
        # 加，分割 2
        name_l.append(x0+'.'+x1)
        if len(x1) !=1:
            name_l.append(x0+'.'+x1[0])
        if return_list: return name_l
        t = random.randrange(0, 2)
        if index=='': return name_l[t]
        if index!='': return name_l[index]
    # 去掉空格 1
    name_l.append(x0+x1)
    name_l.append(x0+x1[0])
    # 加，分割 2
    name_l.append(x0+'.'+x1)
    name_l.append(x0+'.'+x1[0])
    # 首，1
    name_l.append(x0[0]+x1)
    # 首，1
    name_l.append(x0[0]+'.'+x1)
    if return_list: return name_l
    t = random.randrange(0, 4)
    if index=='': return name_l[t]
    if index!='': return name_l[index]


# 生成邮箱
def sc_email(name, end_t, lx,index=''):
    if index==9 or index=='': name = name_gsh(name,index=index)
    if lx == 0:
        end_t = end_t+'.com'
    elif lx == 1:
        end_t = end_t.split('.')[-2]+'.'+end_t.split('.')[-1]
    elif lx == 3:
        end_t = end_t
    email = str(name) + '@' + str(end_t)
    return email


# 验证是否有官网，并且返回邮箱
def yz_website(name, company_e, company_qx, compalist):
    for item in compalist:
        # 只有网址
        item1 = item.split('//')[1].split('/')[0]
        if company_qx[0] in item1:
            return sc_email(name, item1, 1)
    return sc_email(name, company_e, 0)

# 验证是否保存完
def check_save(cx,path,name=''):
    while True:
        if b.isElementExist(cx,path,name=name):
            break
        else:
            time.sleep(random.randrange(1, 2))

# 更改leads
def gg_leads(cx,xpath,ml0,ml1,position=0):
    # 合并文本
    text=ml0+' '+ml1
    b.trwb(cx,xpath,text,position=position)

# 检测move_on是否点击
def ismove_on_click(cx):
    flag = False
    while True:
        try:
            flag = cx.find_element_by_xpath(input_move_on).is_selected()
            return flag
        except:
            time.sleep(random.randrange(1, 2))
            
# 获取公司的首字母组合
def gz3(its):
    x = ''
    for it in its.split():
        x = x + it[0]
    return x.lower()

# 下拉框选择2,index不减一
def select_by_js(cx,xpath,index,position=0):
    while True:
        if not b.isElementExist(cx,xpath+'/div[2]/lightning-base-combobox-item',name='no'):
            b.zxjs1(cx,xpath+'/div[1]/button',position=position) 
        else:
            break
        time.sleep(1)
    b.zxjs1(cx,xpath+f'/div[2]/lightning-base-combobox-item[{index}]',position=position)

# linked in 查找url
def linked_url_makesure(cx,list,option):
    cs=0
    while True:
        cx = webdriver.Chrome(chrome_options=option)
        cx.switch_to.default_content()
        WebDriverWait(cx, 20, 1).until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, f'{iframe_lo}')))
        for i in list:
            i=str(i)
            if b.isElementExist(cx,f'//*[@id="ember{i}"]',name='no'):
                url_open = True
                find_true=True
                idz = i
                break
            else:
                url_open=False
                find_true=False
        if find_true:
            break
        elif cs==5:
            idz=0
            url_open=False
            break
        cs+=1
    return cx,idz,url_open

# 检查list是否有任意元素(不区分大小写)在str中
def check_list_in_str(list,str):
    for i in list:
        if i.lower() in str.lower():
            return True
    return False

# 检测邮箱是否错误
def check_email_right(cx,name_box,email,BDA_Notes):
    time.sleep(1)
    if not b.isElementExist(cx,email_error,name='no') and not b.isElementExist(cx,re_error,name='no'):
        return 'normal',False
    elif b.isElementExist(cx,email_error,name='no') or b.isElementExist(cx,re_error,name='no'):
        name_box_tmp=name_box.copy()
        name_box_tmp.remove(email.split('@')[0])
        for item in name_box_tmp:
            email=item+'@'+email.split('@')[1]
            b.trwb(cx,input_email,email)
            b.zxjs1(cx,save_button_lo)
            # 小数，整数右边不会达到
            time.sleep(3)
            if not b.isElementExist(cx,email_error,name='no') and not b.isElementExist(cx,re_error,name='no'):
                return email,True
            time.sleep(random.randrange(1,3))
        # 几乎不可能
        if b.isElementExist(cx,email_error,name='no'):
            b.trwb(cx,input_email,'')
            gg_leads(cx,input_bda,BDA_Notes,'email')
            b.zxjs1(cx,save_button_lo)
            return '',False