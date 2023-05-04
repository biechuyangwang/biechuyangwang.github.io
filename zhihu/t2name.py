import urllib3
import time
import json
from tkinter import *
import certifi


def pprint(content):
    text.insert(INSERT,content)
    text.insert(INSERT,'\n')

def getExpirationDateFromToken(token):
    """由token获取过期时间

    Args:
        token (_type_): _description_
    """
    import base64
    expirationdate = token.split('.')[1][8:24]
    expirationdate = int(base64.b64decode(expirationdate)[1:-1])
    # expirationdate = time.localtime(int(expirationdate))
    # expirationdate = time.strftime("%Y-%m-%d %H:%M:%S", expirationdate)
    return expirationdate

def getUserInfo():
    """获取个人信息

    Args:
    """
    token = entry.get()

    text.delete(1.0,'end')
    BASE_URL = "https://cat-match.easygame2021.com/sheep/v1/game"
    url = f"{BASE_URL}/personal_info?"
    request_manager = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(), timeout=30)
    headers={
        "Connection": "keep-alive",
        "t": token,
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx141bfb9b73c970a9/66/page-frame.html"
    }
    try:
        response = request_manager.request("GET", url, headers=headers, preload_content=False)
        content = response.read()
        content = json.loads(content)
        response.close()

        pprint(f"{'='*10}本软件由 星期六的故事 提供{'='*10}")
        pprint(f"用户名：{content['data']['nick_name']}")
        pprint(f"t值过期时间：{getExpirationDateFromToken(token)}")
        pprint(f"皮肤数量：{content['data']['skin']}")
        pprint(f"今日是否已通关日常：{'是' if content['data']['today_state'] else '否'}")
        pprint(f"t值：{token}")
        pprint(f"{'='*20}结束{'='*20}")
        return True
    except Exception as e:
        pprint(str(e))
        return None

if __name__ == "__main__":
    # 创建窗口：实例化一个窗口对象。
    root = Tk()

    # 窗口大小
    root.geometry("800x480+347+128")

    #  窗口标题
    root.title("由token获取个人信息")

    frame1 = Frame(root)
    frame2 = Frame(root)
    frame3 = Frame(root)

    # 添加标签控件
    label = Label(frame1,text="输入t(token)值:",font=("宋体",25),fg="black")

    # 定位
    label.grid()

    # 添加输入框
    entry = Entry(frame2,width=30,font=("宋体",25),fg="black")
    entry.grid(row=0,column=0, padx=10)

    # 添加点击按钮
    button = Button(frame2,text="转换",font=("宋体",18),fg="blue",command=getUserInfo)
    button.grid(row=0,column=1)

    # 多行文本
    text = Text(frame3,width=50,autoseparators=True,state="normal",wrap="word",spacing2=4,spacing3=25,tabs=16,font=("宋体",20),fg="black")
    scroll = Scrollbar(frame3,orient=VERTICAL)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.pack(side=LEFT,fill=X)


    frame1.pack(pady=5,fill=X)
    frame2.pack(fill='both')
    frame3.pack(fill='both')

    # 显示窗口
    root.mainloop()