import urllib3
from urllib.parse import quote, unquote,urlencode
import json
import re
from lxml import etree
from tkinter import *
from tkinter import messagebox
import requests

def pprint(content):
    text.insert(INSERT,content)
    text.insert(INSERT,'\n')

def func():
    wd = entry.get()
    headers = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':'gzip, deflate, br',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':'_ga=GA1.1.926273860.1669700725; __gads=ID=eb2d7595676eb4a4-2208e681add800d3:T=1669700725:RT=1669700725:S=ALNI_MY0A05Y_X_R6fbyuTK_2AB9pdacJw; SSLSESSID=d8a18f669305532266f1ada115565a77; __gpi=UID=00000b85b2aa32a7:T=1669700725:RT=1669949461:S=ALNI_MZwuPJOIDEEh8S-kjxYkeNyhyzDOw; _ga_SDWQ8N23LZ=GS1.1.1669949460.7.1.1669951958.0.0.0',
        'origin':'https://www.sxctp.org',
        'referer':'https://www.sxctp.org/search/',
        'sec-ch-ua-platform': "Windows",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    session = requests.Session()
    session.headers = headers

    response = session.get("https://www.sxctp.org")
    res = response.content.decode("utf-8")
    html  = etree.HTML(res)
    __token__ = html.xpath('/html/body/header/nav/div/div/div/form/input[2]')[0]
    if "value" in __token__.attrib:
        token_value = __token__.attrib["value"]

    data = {
        "wd": wd,
        "__token__": token_value
    }
    data = urlencode(data,doseq=True)
    response = session.post("https://www.sxctp.org/search/", data=data)
    res = response.content.decode("utf-8")
    html  = etree.HTML(res)
    url_a = html.xpath('/html/body/div[2]/div[3]/h2/a')[0]
    if "href" in url_a.attrib:
        href = url_a.attrib["href"]
    
    url = 'https://www.sxctp.org' + href
    response = session.get(url)
    res = response.content.decode("utf-8")
    html  = etree.HTML(res)
    title = html.xpath('/html/body/div[2]/div/article/h1')[0]
    content = html.xpath('/html/body/div[2]/div/article/div[2]')[0]
    # article_column = html.xpath('//*[@id="article-column"]/a')[0] #专栏，备用
    # if "href" in article_column.attrib:
    #     href = article_column.attrib["href"]
    title = etree.tostring(title,encoding='utf-8').decode()
    title_cont = re.sub(r'<[^>]*?>','' ,title).strip()
    title_cont = re.sub(r'&#13;','' ,title_cont)
    pprint(f"文章标题:{title_cont}")
    pprint(f"正在生成txt文件和网页文件")
    content = etree.tostring(content,encoding='utf-8').decode()
    content_cont = re.sub(r'<[^>]*?>','' ,content)
    content_cont = re.sub(r'&#13;','' ,content_cont).strip()
    message = f"<html><head><style>img" + "{max-width:100%;}" + f"</style></head><body>{title}\n{content}</body></html>"
    with open(f"{title_cont}.html", "w", encoding="utf-8") as f:
        f.write(message)
    with open(f"{title_cont}.txt", "w", encoding="utf-8") as f:
        f.write(content_cont)
    pprint(f"=====完成=====")
if __name__ == "__main__":
    # 创建窗口：实例化一个窗口对象。
    root = Tk()

    # 窗口大小
    root.geometry("800x480+347+128")

    #  窗口标题
    root.title("知乎盐选解析(By:星期六)")

    frame1 = Frame(root)
    frame2 = Frame(root)

    # 添加标签控件
    label = Label(frame1,text="输入:",font=("宋体",25),fg="black")

    # 定位
    label.grid()

    # 添加输入框
    entry = Entry(frame1,width=30,font=("宋体",25),fg="black")
    entry.grid(row=0,column=1, padx=10)

    # 添加点击按钮
    button = Button(frame1,text="转换",font=("宋体",18),fg="blue",command=func)
    button.grid(row=0,column=2)

    # 多行文本
    text = Text(frame2,width=50,autoseparators=True,state="normal",wrap="word",spacing2=4,spacing3=25,tabs=16,font=("宋体",20),fg="black")
    scroll = Scrollbar(frame2,orient=VERTICAL)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.pack(side=LEFT,fill=X)


    frame1.pack(pady=5,fill=X)
    frame2.pack(fill='both')

    # 显示窗口
    root.mainloop()
    # wd = "闲得无聊，我在暗网上雇了两个人互相追杀对方。"
    # # wd = "https://www.zhihu.com/answer/2582002523"
    # func(wd)