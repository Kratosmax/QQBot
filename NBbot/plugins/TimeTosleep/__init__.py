from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='0,7-23')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        # if now.hour > 6:
        await bot.send_group_msg(group_id=187170914, message=f'西瓜为你准点报时:现在是{now.hour}点整')
        await bot.send_group_msg(group_id=217982742, message=f'西瓜为你准点报时:现在是{now.hour}点整')
    except CQHttpError:
        pass
