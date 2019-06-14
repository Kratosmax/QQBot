from nonebot import on_notice,NoticeSession,on_request,RequestSession,MessageSegment

@on_request('group')
async def _(session: RequestSession):
    if(session.ctx['group_id'] == 555877621):
        await session.approve()
    return

@on_notice('group_increase')
async def _(session: NoticeSession):
    # 发送欢迎消息
    print(session.ctx['user_id'])
    msg =MessageSegment.at(session.ctx['user_id']) +' ' + MessageSegment.text('请新进群的小伙伴，按照公告内的要求改好自己的群名片，并仔细阅读本群所有公告~，进群先看群文件和群相册，看完有问题再问')
    await session.send(msg)

