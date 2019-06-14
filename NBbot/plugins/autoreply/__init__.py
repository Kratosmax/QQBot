from nonebot import on_natural_language, NLPSession, MessageSegment
import json
import re
import jieba

print("读取自动回复关键字")
# kwf = open('res/kw.json', encoding='utf-8')
f1 = open('res/Q.json', encoding='utf-8')
f2 = open('res/A.json', encoding='utf-8')
# kw = json.loads(kwf.read())
Qconf = json.loads(f1.read())
Aconf = json.loads(f2.read())

tmp_str = ''
ban_str = ''


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    global tmp_str, ban_str
    if session.ctx['raw_message'] == tmp_str:
        if not ban_str:
            ban_str = True
            await session.send(tmp_str)
    else:
        ban_str = False
        tmp_str = session.ctx['raw_message']
        msg_num = wordCut(tmp_str)
        if msg_num:
            msg = MessageSegment.at(
                session.ctx['user_id']) + " " + Aconf[msg_num]
            await session.send(msg)
        else:
            return


def wordCut(msg):
    for key, value in Qconf.items():
        kw = value
        res = re.findall(kw, msg)
        print(res)
        if (len(res)):
            return key
    return False
