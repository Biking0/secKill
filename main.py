

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import threading

#时钟间隔
ti=0.001
#秒杀时间
buytime="2018-09-05 23:59:00"

#配置账号密码
name="username"
pwd="password"

#创建8个浏览器
browser1= webdriver.Chrome("D:\softInstall\chromedriver.exe")
browser2= webdriver.Chrome("D:\softInstall\chromedriver.exe")
browser3= webdriver.Chrome("D:\softInstall\chromedriver.exe")
browser4= webdriver.Chrome("D:\softInstall\chromedriver.exe")
browser5= webdriver.Chrome("D:\softInstall\chromedriver.exe")
browser6= webdriver.Chrome("D:\softInstall\chromedriver.exe")
browser7= webdriver.Chrome("D:\softInstall\chromedriver.exe")
browser8= webdriver.Chrome("D:\softInstall\chromedriver.exe")


#创建8个方法
def bro1():

    browser1.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser1.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser1.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser1.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)

    browser1.get("https://www.mi.com/seckill/")

    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                try :
                    browser1.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[1]/div[2]/a[1]').click() #购买按钮的Xpath
                # browser1.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！1')

        time.sleep(ti)#注意刷新间隔时间要尽量短
def bro2():

    browser2.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser2.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser2.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser2.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)

    browser2.get("https://www.mi.com/seckill/")

    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                try :
                    browser2.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[1]/div[2]/a[2]').click() #购买按钮的Xpath
                # browser1.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！2')

        time.sleep(ti)#注意刷新间隔时间要尽量短
def bro3():

    browser3.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser3.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser3.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser3.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)

    
    browser3.get("https://www.mi.com/seckill/")
    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
           while True:
                try :
                    browser3.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[1]/div[2]/a[3]').click() #购买按钮的Xpath
                # browser1.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！2')

        time.sleep(ti)#注意刷新间隔时间要尽量短
def bro4():

    browser4.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser4.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser4.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser4.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)
    
    browser4.get("https://www.mi.com/seckill/")
    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                try :
                    browser4.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[1]/div[2]/a[4]').click() #购买按钮的Xpath
                # browser1.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！2')

        time.sleep(ti)#注意刷新间隔时间要尽量短
def bro5():

    browser5.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser5.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser5.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser5.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)
    browser5.get("https://www.mi.com/seckill/")
    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                try :
                    browser5.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[3]/div[2]/a[5]').click() #购买按钮的Xpath
                # browser1.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！2')

        time.sleep(ti)#注意刷新间隔时间要尽量短
def bro6():
    browser6.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser6.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser6.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser6.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)

    browser6.get("https://www.mi.com/seckill/")
    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                try :
                    browser6.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[3]/div[2]/a[6]').click() #购买按钮的Xpath
                # browser1.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！2')

        time.sleep(ti)#注意刷新间隔时间要尽量短
def bro7():

    browser7.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser7.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser7.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser7.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)

    browser7.get("https://www.mi.com/seckill/")
    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                try :
                    browser7.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[3]/div[2]/a[7]').click() #购买按钮的Xpath
                # browser1.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！2')

        time.sleep(ti)#注意刷新间隔时间要尽量短
def bro8():

    browser8.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser8.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser8.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser8.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)

    browser8.get("https://www.mi.com/seckill/")
    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                try :
                    browser8.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[3]/div[2]/a[8]').click() #购买按钮的Xpath
                # browser1.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！8')

        time.sleep(ti)#注意刷新间隔时间要尽量短

#使用线程
t1=threading.Thread(target=bro1)
t2=threading.Thread(target=bro2)
t3=threading.Thread(target=bro3)
t4=threading.Thread(target=bro4)
t5=threading.Thread(target=bro5)
t6=threading.Thread(target=bro6)
t7=threading.Thread(target=bro7)
t8=threading.Thread(target=bro8)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()



    
