import urllib3
import json
import re
from lxml import etree
import xmltodict
from tkinter import *
from tkinter import messagebox

def pprint(content):
    text.insert(INSERT,content)
    text.insert(INSERT,'\n')

def func():
    data = entry.get()
    pprint(f"开始解析:{entry.get()}")
    http = urllib3.PoolManager()
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'Host':'onehu.xyz'}
    
    # data = {"url":["https://www.zhihu.com/answer/2582002523"]}
    # url = 'https://mfyx.top/'
    # data = json.dumps(data).encode()
    response = http.request('GET','https://onehu.xyz/feed.xml',headers=headers)
    content = response.data.decode('utf-8')
    xmlparse = xmltodict.parse(content)
    # jsonstr = json.dumps(xmlparse,indent=1,ensure_ascii=False)
    jsonstr = xmlparse['rss']['channel']['item']
    true_url = ""
    for item in jsonstr:
        if data in item['title'] or data in item["description"]:
            true_url = item['link']
            break
    # print(true_url)

    if true_url:
        pprint(f"引擎一解析成功，请稍等。。。")
        response = http.request('GET',true_url, headers=headers,)
        res = response.data.decode('utf-8')
        html  = etree.HTML(res)
        title = html.xpath('//*[@id="page-info"]/h1/text()')[0]
        content = html.xpath('//*[@id="post-content"]/div')[0]
    else:
        pprint(f"引擎一解析失败，启动引擎二，请稍等。。。")
        # f"https://ifun.cool/?s={data}&type=post"
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        response = http.request('GET',f"https://ifun.cool/?s={data}&type=post",headers=headers)
        content = response.data.decode('utf-8')
        html  = etree.HTML(content)
        url_a = html.xpath('/html/body/main/div[1]/div/div[2]/posts[1]/div/h2/a')[0]
        href = ""
        if "href" in url_a.attrib:
            href = url_a.attrib["href"]
            pprint(f"引擎二解析成功，请稍等。。。")
        else:
            pprint(f"解析失败，该文章未收录")
            return
        # print(href)
        
        response = http.request('GET',href, headers=headers,)
        res = response.data.decode('utf-8')
        html  = etree.HTML(res)
        title = html.xpath('/html/body/main/div[1]/div/article/div[1]/h1/a/text()')[0]
        content = html.xpath('/html/body/main/div[1]/div/article/div[2]/div[1]')[0]
        # url /html/body/main/div[1]/div/div[2]/posts[1]/div/h2/a
        # title /html/body/main/div[1]/div/article/div[1]/h1/a
        # content /html/body/main/div[1]/div/article/div[2]/div[1]


    # title = etree.tostring(title,encoding='utf-8').decode()
    title_cont = re.sub(r'<[^>]*?>','' ,title).strip()
    title_cont = re.sub(r'^[0-9]+','' ,title_cont)
    pprint(f"文章标题:{title_cont}")
    pprint(f"正在生成txt文件和网页文件")
    content = etree.tostring(content,encoding='utf-8').decode()
    content_cont = re.sub(r'<[^>]*?>','' ,content)
    message = f"""<html>
    <head></head>
    <body>{title_cont}\n{content}</body>
    </html>"""
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
    label = Label(frame1,text="盐选链接:",font=("宋体",25),fg="black")

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



# print(response.status,response.data.decode('utf-8'))