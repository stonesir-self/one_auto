# -*- coding: UTF-8 -*-
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
# os.system('pause')
# code.interact(banner="", local=locals())
# import os
# os.environ["http_proxy"] = "http://127.0.0.1:30809"
# os.environ["https_proxy"] = "http://127.0.0.1:30809"
# time.sleep(random.randrange(2, 5))


# 检测元素是否存在
def isElementExist(cx, xp, position=0,name=''):
    flag = True
    try:
        cx.find_elements_by_xpath(xp)[position]
        return flag
    except:
        if name != 'no': print(name+'元素未找到!')
        flag = False
        return flag


# 第二个为元素位置，0为第一个,会一直找到
def hqwb(cx, path, name='',position=0):
    while True:
        if isElementExist(cx, f'{path}',name=name):
            break
        else:
            time.sleep(random.randrange(1, 3))
    while True:
        try:
            item = cx.find_elements_by_xpath(
                f'{path}')[position].text
            break
        except:
            time.sleep(random.randrange(1, 2))
    return item


# 检测元素是否可点击, 会一直等待，直到可点击
def iselement_enabled(cx, path, name='',position=0):
    flag = False
    while True:
        try:
            flag = cx.find_elements_by_xpath(
                f'{path}')[position].is_enabled()
            return flag
        except:
            print(name+'元素可点击测试失败!')
            time.sleep(random.randrange(1, 2))


# 点击，正常点击
def dj(cx, path, lx, name='',position=0):
    iselement_enabled(cx, path, name=name,position=position)
    if lx == 'click':
        cx.find_elements_by_xpath(path)[position].click()
    elif lx == 'enter':
        cx.find_elements_by_xpath(path)[position].send_keys(Keys.ENTER)
    else:
        print(name+'点击类型错误，请检查')
        return False
    return True


# 执行js(按classname),第一个为class，第二个为位置，(0开始,浏览器数字要减一)
def zxjs0(cx, class_, position=0):
    js = class_
    jsml = f"document.getElementsByClassName('{class_}')[{position}].click()"
    cx.execute_script(jsml)


# 执行js，xpath, (0开始,浏览器数字要减一)
def zxjs1(cx, path, position=0):
    element = cx.find_elements_by_xpath(path)[position]
    cx.execute_script("arguments[0].click();", element)


# 填入文本
def trwb(cx, xpath, text,position=0):
    # 更改leads
    cx.find_elements_by_xpath(
        xpath)[position].clear()
    cx.find_elements_by_xpath(
        xpath)[position].send_keys(text)


# 时间间隔 time0 = time.time()
def timediff_to_str2(timestamp, timestamp1):
    onlineTime = datetime.fromtimestamp(timestamp)
    localTime = datetime.fromtimestamp(timestamp1)
    result = localTime - onlineTime
    hours = int(result.seconds / 3600)
    minutes = int(result.seconds % 3600 / 60)
    seconds = result.seconds % 3600 % 60
    return "{0}天{1}时{2}分{3}秒".format(result.days, hours, minutes, seconds)


# 切换iframe,第二个为切换成功的验证，可以为一个元素的xpath
def iframe_qhyz(cx,xpath,yzpath,chrome_options1,position=0):
    while True:
        WebDriverWait(cx, 20, 2).until(EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, xpath)))
        if isElementExist(cx,yzpath):
            return True
        cx = webdriver.Chrome(chrome_options=chrome_options1)
        cx.switch_to.default_content()


# -1为最右边的窗口，0为最左边窗口,默认是最右边窗口,(driver.switch_to.default_content())
def swich_default_window(cx,position=-1):
    handles = cx.window_handles
    cx.switch_to.window(handles[position])


# 鼠标悬浮
def mouse_hold(cx,xpath,position=0):
    # mouse = cx.find_element_by_link_text("设置")
    mouse = cx.find_elements_by_xpath(xpath)[position]
    ActionChains(cx).move_to_element(mouse).perform()

# 下拉框选择
# position代表元素，要减1,index,从最后开始数,不变
def select_by_elements_index(cx,path, index,direction='down',position=0):
    if direction=='up':
        for i in range(index):
            iselement_enabled(cx,path) and cx.find_elements_by_xpath(
                f'{path}')[position].send_keys(Keys.UP)
            time.sleep(random.uniform(0, 1))
    elif direction=='down':
        for i in range(index):
            iselement_enabled(cx,path) and cx.find_elements_by_xpath(
                f'{path}')[position].send_keys(Keys.DOWN)
            time.sleep(random.uniform(0, 1))
    else:
        print('方向输入错误!')
    iselement_enabled(cx,f'{path}') and cx.find_elements_by_xpath(
        f'{path}')[position].send_keys(Keys.ENTER)