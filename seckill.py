
#网上参考原版

from selenium import webdriver
import time
import datetime
 
browser = webdriver.Chrome("D:\softInstall\chromedriver.exe")
 
def login(name ,pwd):
    browser.get( 'https://account.xiaomi.com/')#登录网址
    time.sleep(2)
    browser.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)
    
    print('登录成功，正在等待秒杀···')
 
def buy_on_time(buytime):
    browser.get("https://www.mi.com/seckill/")#切换到秒杀页面
    while True: #不断刷新时钟
        now = datetime.datetime.now()
        # if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
        browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[6]/div[2]/a[2]').click() #购买按钮的Xpath
        browser.find_element_by_xpath('/html/body').click() #取消提醒
        print('下单成功，请抓紧付款！')

        time.sleep(0.6)#注意刷新间隔时间要尽量短


#配置账号密码
# login('username' , 'password')
buy_on_time('2018-06-07 21:25:00')#指定秒杀时间，并且开始等待秒杀
 
