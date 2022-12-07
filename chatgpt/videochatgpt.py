import asyncio
from bilibili_api import video
from bilibili_api import comment, sync
async def main():
    # 实例化 Video 类
    v = video.Video(bvid="BV1K84y1r7ci")
    aid = v.get_aid()
    # 存储评论
    comments = []
    # 页码
    page = 1
    # 当前已获取数量
    count = 0
    while True:
        # 获取评论
        c = await comment.get_comments(aid, comment.CommentResourceType.VIDEO, page)
        # print(str(c))
        # oid = c['replies'][0]['oid']
        # rpid = c['replies'][0]['rpid']
        # sub_c = comment.Comment(oid,comment.CommentResourceType.VIDEO,rpid,None)
        # subcontent = await sub_c.get_sub_comments(1)
        # print(str(subcontent))

        # 存储评论
        comments.extend(c['replies'])
        # 增加已获取数量
        count += c['page']['size']
        # 增加页码
        page += 1

        if count >= c['page']['count']:
            # 当前已获取数量已达到评论总数，跳出循环
            break

    # 打印评论
    for cmt in comments:
        print(f"{cmt['member']['uname']}: {cmt['content']['message']}")

    # 打印评论总数
    print(f"\n\n共有 {count} 条评论（不含子评论）")
    # # 获取信息
    # info = await v.get_info()
    # # 打印信息
    # print(info)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())