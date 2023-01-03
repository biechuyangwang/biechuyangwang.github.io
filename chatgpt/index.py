import os
import openai
openai.organization = "org-9bjRYTQd2v3D7xfqalH4nwP2"
openai.api_key = "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"
# print(openai.Model.list())

def reply_text(query):
    try:
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt=query,
            temperature=0.9,  # 值在[0,1]之间，越大表示回复越具有不确定性
            max_tokens=100,  # 回复最大的字符数
        )
        res_content = res.choices[0]["text"].strip()
    except Exception as e:
        return None
    return res_content
# res = reply_text("你好啊~")
# print(res)

def create_img(query, size=256):
    try:
        res = openai.Image.create(
            prompt=query,
            n=1,
            size=f"{size}x{size}"
        )
        image_url = res['data'][0]['url']
    except Exception as e:
        return None
    return image_url
# res = create_img("一个坐在湖边的美丽少女，光着脚泡在水里。湖边有柳树，湖里有游动的鱼群，黄昏",1024)
# print(res)
# {
#   "created": 1589478378,
#   "data": [
#     {
#       "url": "https://..."
#     },
#     {
#       "url": "https://..."
#     }
#   ]
# }