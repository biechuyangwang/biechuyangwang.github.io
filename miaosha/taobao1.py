# 购物车秒杀程序
# 注意，需要将商品提前加入购物车
# 订单抢到后，请在30分钟内支付
import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
print(now)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# import win32com.client # 用来播报语音
# speaker = win32com.client.Dispatch("SAPI.SpVoice")

pre_time = "2022-12-20 14:17:00.00000000"
# webtools = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
webtools = webdriver.Chrome(chrome_options = options)

webtools.get("https://www.taobao.com/") # 打开淘宝或者京东
time.sleep(4)

# webtools.find_element_by_link_text("亲，请登录").click() # 准备扫码登录，这是旧版本的，需要使用新版本方法
webtools.find_element(By.LINK_TEXT, "亲，请登录").click()

print(f"请尽快扫码登录")
time.sleep(20) # 给你10秒去扫码登录

webtools.get("https://cart.taobao.com/cart.htm") # 进入购物车
time.sleep(4)

while True:
    try:
        if webtools.find_element(By.ID,"J_SelectAll1"):
            webtools.find_element(By.ID,"J_SelectAll1").click()
            break
    except:
        print(f"找不到全选按钮")

while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"当前时间:{now}")
    if now > pre_time:
        while True:
            try:
                if webtools.find_element(By.LINK_TEXT, "结 算"):
                    webtools.find_element(By.LINK_TEXT, "结 算").click()
                    print(f"已经锁定商品")
                    break
            except:
                pass
        while True:
            try:
                if webtools.find_element(By.LINK_TEXT, "提交订单"):
                    webtools.find_element(By.LINK_TEXT, "提交订单").click()
                    print(f"抢购成功，请尽快付款")
                    break
            except:
                print(f"请及时支付订单")






