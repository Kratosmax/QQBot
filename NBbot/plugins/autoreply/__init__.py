from nonebot import on_natural_language, NLPSession, MessageSegment
import json
import re
import jieba

print("读取自动回复关键字")
# kwf = open('res/kw.json', encoding='utf-8')
f1 = open('res/Q.json', encoding='utf-8')
f2 = open('res/A.json', encoding='utf-8')
f3 = open('res/fdgroups.json', encoding='utf-8')
# kw = json.loads(kwf.read())
Qconf = json.loads(f1)
Aconf = json.loads(f2)
groupconf = json.load(f3)
f1.close()
f2.close()
f3.close()

tmp_dict = {}
ban_dict = {}
for group in groupconf:
    tmp_dict[group] = ''
    ban_dict[group] = False


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    global tmp_dict, ban_dict
    if session.ctx['message_type'] == 'group':  # 判断是否为群信息
        gid = session.ctx['group_id']           # 获取群号
        if session.ctx['raw_message'] == tmp_dict[gid]:
            if not ban_dict[gid]:
                ban_dict[gid] = True
                await session.send(tmp_dict[gid])
        else:
            ban_dict[gid] = False
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
