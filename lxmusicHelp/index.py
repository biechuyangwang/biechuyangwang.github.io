import json
from urllib.parse import quote
import playwright

func = "播放歌曲" # 功能名，支持打开歌单、播放歌单、搜索歌曲、播放歌曲
name = "青花瓷" # 歌曲名
singer = "" # 艺术家名
source = "tx" # 源，支持kw/kg/tx/wy/mg
func_list = {
    "打开歌单":"songlist/open",
    "播放歌单":"songlist/play",
    "搜索歌曲":"music/search",
    "播放歌曲":"music/play",
}
data = {
    "打开歌单":{
    "source":"tx", # 支持 kw/kg/tx/wy/mg
    "id":"",
    "url":"", # id和url必须传一个
    },
    "播放歌单":{
    "id":"",
    "url":"", # id和url必须传一个
    "index":0, # 播放第几首，从0开始
    },
    "搜索歌曲":{
    "keywords":name,
    "source":source,
    },
    "播放歌曲":{
    "name":name, # 歌曲名，必须
    "singer":singer, # 艺术家，必须
    "source":source, # 源，必须
    "songmid":"", # 歌曲id，必须
    "img":"", # 歌曲图片了解，选传
    "albumId":"", # 歌曲专辑id，选传
    "interval":"", # 格式化后歌曲时长，选传，例如 03:55
    "albumName":"", # 歌曲专辑名称，宣传
    "types":[{"type":"flac", "size":"","hash":""}], # type 128k/320k/flac/flac24bit
    "hash":"", # kg必须
    "strMediaMid":"", # tx必传
    "copyrightId":"", # tx选传
    "lrcUrl":"", # mg选传
    },
}


data1 = f"{json.dumps(data[func],ensure_ascii=False)}"
print(data1)
url = f"lxmusic://{func_list[func]}?data={data1}"
print(repr(url))
a = "www.baidu.com"
print(repr(a))

import time
from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.click('input[name="wd"]')
    page.click('text="京东"')
    # page.goto('lxmusic://music/play?data={"name": "青花瓷", "singer": "", "source": "tx", "songmid": "", "img": "", "albumId": "", "interval": "", "albumName": "", "types": [{"type": "flac", "size": "", "hash": ""}], "hash": "", "strMediaMid": "", "copyrightId": "", "lrcUrl": ""}')
    time.sleep(10)
    # ---------------------
    # context.close()
    # browser.close()

with sync_playwright() as playwright:
    run(playwright)

# url = f"lxmusic://{func_list[func]}?data={json.dumps(data[func],ensure_ascii=True)}"
# print("编码后的url：",repr(url))