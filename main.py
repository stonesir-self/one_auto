# -*- coding: UTF-8 -*-
from pickle import FALSE
from turtle import position
import chardet
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
import unicodedata
import my_b
from my_b import b_selenum as b
from base.main_fun.py import *
from my_location import *
from other_lo import *

# 获取linked in 的url
def hq_linked_in_url():
    global url_open
    global driver
    (driver,idz,url_open)=linked_url_makesure(driver,idz_list,chrome_options)
    linked_url=False
    if url_open:
        html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
        soup = BeautifulSoup(html, 'lxml')
        try:
            linked_url = soup.find('a', {'id': f'ember{idz}'})['href']
            url_open=True
        except:
            linked_url = False
            url_open=False
    b.swich_default_window(driver,position=0)
    return linked_url

# 打开linked 返回tuple
def dklinked_in(url):
    global tr
    comlist=[]
    datlist=[]
    sjdict={}
    # 打开linked
    new = f'window.open("{url}")'
    driver.execute_script(new)
    time.sleep(random.randrange(1, 2))
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    time.sleep(random.randrange(2, 5))
    while True:
        try:
            html = driver.find_element_by_xpath(
                "//*").get_attribute("outerHTML")
            break
        except:
            time.sleep(random.randrange(2, 5))
    # 获取公司比对数据
    soup = BeautifulSoup(html, 'lxml')
    # 获取公司名称
    for tr in soup.findAll('li', {'class': "profile-position display-flex align-items-flex-start"}):
        if isinstance(tr, bs4.element.Tag):
            try:
                tds = tr.findAll('span')[1].text.strip()
            except:
                tds = ''
            comlist.append(tds)
    # 获取在职时间
    for tr in soup.findAll('li', {'class': "profile-position display-flex align-items-flex-start"}):
        if isinstance(tr, bs4.element.Tag):
            try:
                tds = tr.find(
                    'p', {'class': "profile-position__dates-employed fl t-12 t-black--light"}).text.strip().replace(
                    'Dates Employed\n                \n                ', '')
            except:
                tds = ''
            datlist.append(tds)
    # 总数据
    for tr in soup.findAll('li', {'class': "profile-position display-flex align-items-flex-start"}):
        if isinstance(tr, bs4.element.Tag):
            try:
                tds = tr.findAll('span')[1].text.strip()
            except:
                tds = ''
            try:
                tds2 = tr.find(
                    'p', {'class': "profile-position__dates-employed fl t-12 t-black--light"}).text.strip().replace(
                    'Dates Employed\n                \n                ', '')
            except:
                tds2 = ''
            sjdict[tds] = tds2
    driver.close()
    return comlist,datlist,sjdict

# email_history
def email_history(charde_name,email):
    name_box=name_gsh(charde_name)
        
# 公司首字母判断
def company_szm_pd(item):
    if len(gz3(f'{company0}')) >= 3 and gz3(f'{company0}') in item.lower():
        return True
    else:
        return False

# 准备浏览器
def llq():
    global driver
    global chrome_options
    # driver = webdriver.Chrome()
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument(
    #     '--user-data-dir=D:\\gg-work')
    # chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option(
        "debuggerAddress", "127.0.0.1:52902")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver.get(f"{url}")
    # print(driver.title)
    driver.implicitly_wait(3)  # seconds
    kszy()

'''
加入了bda_original
'''
# 开始作业
def kszy():
    global comlist
    global datlist
    global sjdict
    global company
    global driver
    global leads_status
    global company0
    global BDA_Notes
    global tr
    global url_open
    global rejected_reson
    global account_name
    global rejected_details
    global time1
    global gs
    global cw_l
    global re_l
    global recent_st
    global email
    global email_st
    global email_dict
    global title_st
    global bda_origin_st
    # 点击人物
    dj_sure(driver,first_item,detail_lo,'enter',name='点击人物',name2='no')
    # 获取linked inurl
    linked_in_url=hq_linked_in_url()
    # 点击Details
    dj_sure(driver,detail_lo,change_lo,'enter',name='点击detail',name2='no')
    # 获取 email
    email=hqwb_noerror(driver,email_lo)
    # recycle start
    bda_origin=hqwb_noerror(driver,bda_original_lo)
    if check_list_in_str(recycle_list,bda_origin):
        print('源地区错误')
        bda_origin_st=True
        url_open = False
    # recycle end
    # 获取 name
    chardet_name=hqwb_noerror(driver,name_lo)
    chardet_name=str(unicodedata.normalize('NFKD', chardet_name).encode('ascii','ignore'),'UTF-8')
    # 获取BDA_Notes
    BDA_Notes=hqwb_noerror(driver,BDA_Notes_lo,position=-1)
    if check_list_in_str(my_bda_list,BDA_Notes):
        print('leads错误, 重新打开!')
        time.sleep(random.randrange(1,3))
        b.dj(driver,close_button_lo,'enter',name='关闭按钮')
        gs -= 1
        cw_l += 1
        return
    # 获取title
    BDA_title=hqwb_noerror(driver,BDA_title_lo)
    if sz_title != '' and sz_title.lower() not in BDA_title.lower():
        print('leads_title错误, 重新打开!')
        title_st = True
        url_open = False
    # 获取右上角状态，recent
    recent=hqwb_noerror(driver,recent_lo,position=-1)
    if 'We found no potential duplicates of this Lead.' not in recent:
        print('最近做过')
        re_l += 1
        recent_st = True
        url_open = False
    # 获取 company,小写
    company0=hqwb_noerror(driver,company_lo).lower()
    company=company_format(company0)
    company_gg=company_format(company0,jg='+')
    # 生成 company_email(等于了email)
    company_email=make_company_email_hz(company0)
    name_box=name_gsh(chardet_name,return_list=True)
    email_dict_list_c=[i for i in email_dict.keys()]
    # 生成邮箱
    if email == '':
        if company0 in email_dict_list_c:
            # 有记录
            try:
                sc_email_name=name_box[int(email_dict[company0].split(',')[0])]
            except:
                sc_email_name=name_gsh(chardet_name)
            email=sc_email(sc_email_name, email_dict[company0].split(',')[1], 3,index=email_dict[company0].split(',')[0])
            email_st = True
        else:
            # 无记录
            email = yz_website(chardet_name, company_email, company.split(),
                            google_yz_yx(company_gg))
            email_st = True
    if company0 not in email_dict_list_c:
        try:
            x=name_box.index(email.split('@')[0])
        except:
            # 都不匹配系列,first
            x=9
        email_dict[company0]=str(x)+','+email.split('@')[1]
    # 都不匹配系列,second
    elif company0 in email_dict_list_c and email_dict[company0].split(',')[0]==9:
        email_dict[company0]=str(name_box.index(email.split('@')[0]))+','+email.split('@')[1]
    # 获取leads status
    leads_status=hqwb_noerror(driver,leads_status_lo)
    # 获取rejected_reson
    rejected_reson=hqwb_noerror(driver,rejected_reson_lo)
    # 获取rejected_details
    rejected_details=hqwb_noerror(driver,rejected_details_lo)
    # 获取account_name
    account_name=hqwb_noerror(driver,account_name_lo)
    if url_open:
        (comlist,datlist,sjdict)=dklinked_in(linked_in_url)
    # 恢复主窗口
    b.swich_default_window(driver,position=0)
    # 点击Lead_Status
    b.dj(driver,change_lo,'enter',name='修改')
    open_gz()
    # 保存
    b.dj(driver,save_button_lo,'enter',name='保存按钮')
    # b.zxjs1(driver,save_button_lo)
    # 检测邮箱是否错误, 只有有邮箱，需要改才会触发错误，不需要改email_dict
    (email,check_email_right_return)=check_email_right(driver,name_box,email,BDA_Notes)
    if check_email_right_return:
        email_dict[company0]=str(name_box.index(email.split('@')[0]))+','+email.split('@')[1]
    # 验证是否保存完
    check_save(driver,change_lo,name='no')
    # 关闭当前leads
    b.dj(driver,close_button_lo,'enter',name='关闭按钮')
    # b.zxjs1(driver,close_button_lo)
    # 单个时间
    time1 = time.time()
    time.sleep(random.randrange(1,3))

# good,action
def gg_leads_status():
    global gs_g
    time.sleep(random.uniform(0,2))
    # lead_status
    # b.select_by_elements_index(driver, input_leads_Status,2,position=0)
    select_by_js(driver,input_leads_Status,2)
    # 检测move_on
    if ismove_on_click(driver):
        driver.find_elements_by_xpath(input_move_on)[0].send_keys(Keys.SPACE)
    time.sleep(random.randrange(1,3))
    # 检测reject_reson
    if rejected_reson != '':
        if account_name == '':
            select_by_js(driver,input_reject_reson,1)
        else:
            select_by_js(driver,input_reject_reson,1)
    # 清除reson
    if rejected_details != '':
        b.trwb(driver,input_reject_detail,'')
    if email_st:
        b.trwb(driver,input_email,email)
    time.sleep(random.randrange(1,3))
    gg_leads(driver,input_bda,BDA_Notes,'ok')
    gs_g += 1

# move_on,action
def move_on_leads():
    global gs_m
    time.sleep(random.uniform(0,2))
    # lead_status
    select_by_js(driver,input_leads_Status,11)
    # 检测move_on
    if not ismove_on_click(driver):
        driver.find_elements_by_xpath(input_move_on)[0].send_keys(Keys.SPACE)
    time.sleep(random.randrange(1,3))
    # reject_reson
    if account_name == '':
        select_by_js(driver,input_reject_reson,2)
    else:
        select_by_js(driver,input_reject_reson,2)
    # 更改move_on
    time.sleep(random.randrange(1,3))
    gg_leads(driver,input_bda,BDA_Notes,'move on')
    gs_m += 1

# 判断规则(第一个为在职，或者无公司，找不到)
def open_gz():
    # recycle
    if bda_origin_st:
        time.sleep(1)
        gg_leads(driver,input_bda,BDA_Notes,'n_international')
        return
    # title 不对
    if title_st == True:
        time.sleep(1)
        gg_leads(driver,input_bda,BDA_Notes,'wrong_title')
        return
    # recent 最近做过
    if recent_st == True:
        time.sleep(1)
        gg_leads(driver,input_bda,BDA_Notes,'recent')
        return
    # 判断规则(第一个和空列表选择)
    if len(comlist) == 0:
        gg_leads_status()
        return
    # 找不到
    for item in comlist:
        if company.lower() not in item.lower() and company.split()[0].lower() not in item.lower() and not company_szm_pd(item):
            item_cz = True
        else:
            item_cz = False
            break
    if item_cz:
        gg_leads_status()
        return
    find_ture=False
    for item in comlist:
        iteml=item.lower()
        # 第一个 and present
        if (company in iteml or company.split()[int(0)] in iteml or company_szm_pd(item)) and 'Present' in datlist[comlist.index(f'{item}')] and comlist.index(f'{item}') == 0:
            gg_leads_status()
            find_ture = True
            break
        # 找到为present但不在第一个
        elif (company in iteml or company.split()[int(0)] in iteml or company_szm_pd(item)) and 'Present' in datlist[comlist.index(f'{item}')] and comlist.index(f'{item}') != 0:
            move_on_leads()
            find_ture = True
            break
        # 找到但是没有present
        elif (company in iteml or company.split()[int(0)] in iteml or company_szm_pd(item)) and 'Present' not in datlist[comlist.index(f'{item}')]:
            move_on_leads()
            find_ture = True
            break
    if not find_ture:
        gg_leads(driver,input_bda,BDA_Notes_lo,'-')

if __name__ == '__main__':
    sjdict = {}
    comlist = []
    datlist = {}
    email_dict={}
    i=0
    # 防止打开错误的验证list 
    my_bda_list=['ok','move on','recent','-','wrong_title','call','email','n_international']
    # recycle的错误leads,要关闭将其清空就好
    recycle_list=['international','india','unfound']
    # true为title错误
    title_st = False
    # true为recent错误
    recent_st = False
    # true为email 没有
    email_st = False
    # 做recycle时的original验证
    bda_origin_st=False
    # 初始时间
    time0 = time.time()
    # 总个数
    gs = 1
    # good 个数
    gs_g = 0
    # move on 个数
    gs_m = 0
    # 错误次数
    cw_l = 0
    # recent 次数
    re_l = 0
    # 设置title
    sz_title=''
    llq()
    while True:
        if recent_st:
            time.sleep(random.randrange(2, 4))
        b.swich_default_window(driver,position=0)
        leads_0 = b.hqwb(driver,first_item_bdanote,name='第一人')
        while True:
            if leads_0 == '':
                leads_0 = b.hqwb(driver,first_item_bdanote,name='第一人')
            else:
                break
        if check_list_in_str(my_bda_list,leads_0):
            if i == 1:
                driver.refresh()
                try:
                    WebDriverWait(driver, 10, 2).until(EC.element_to_be_clickable(
                        (By.XPATH, f'{first_item}')))
                    i += 1
                except:
                    time.sleep(5)
                continue
            elif i < 5:
                i += 1
                time.sleep(random.randrange(3, 5))
                continue
            else:
                print(f'目前已做{gs}个, good: {gs_g}个, move_on: {gs_m}个, leads失败次数: {cw_l}, recent个数: {re_l}, 总耗时: ' +
                      b.timediff_to_str2(time0, time1))
                break
        else:
            print(f'目前已做{gs}个, good: {gs_g}个, move_on: {gs_m}个, leads失败次数: {cw_l}, recent个数: {re_l}, 总耗时: ' +
                  b.timediff_to_str2(time0, time1))
            comlist = []
            datlist = []
            sjdict = {}
            recent_st = False
            title_st = False
            email_st = False
            bda_origin_st=False
            i = 0
            gs += 1
            kszy()
