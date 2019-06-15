from nonebot import on_notice, NoticeSession, on_request, RequestSession, MessageSegment, get_bot

bot = get_bot()
@on_request('group')
async def _(session: RequestSession):
    if(session.ctx['group_id'] == 555877621):
        await session.approve()
    return


@on_notice('group_increase')
async def _(session: NoticeSession):
    msg = MessageSegment.at(session.ctx['user_id']) + ' ' + MessageSegment.text(
        '欢迎新进群的小伙伴：\n请按照群公告的要求改好自己的【群名片】,并仔细阅读本群【所有公告】和【2019帮助文档】，进群先看【群文件和群相册】，看完有问题再问，为了让你安心看群文件，先禁言三分钟哈~请见谅')
    await session.send(msg)
    await bot.set_group_ban(group_id=session.ctx['group_id'], user_id=session.ctx['user_id'], duration=180)
