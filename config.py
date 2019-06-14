from nonebot.default_config import *
from datetime import timedelta
SUPERUSERS = {1172616585, 645498469}
COMMAND_START = {'', '/', '／'}
HOST = '0.0.0.0'
PORT = 8080
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=3)
SESSION_RUN_TIMEOUT = timedelta(seconds=15)
SESSION_RUNNING_EXPRESSION = '西瓜有点蠢，还在处理上一条命令'
SESSION_CANCEL_EXPRESSION = (
    '好的',
    '好的吧',
    '行吧，爱咋地咋地',
    '要是我再快点你就取消不了了，可惜了...',
)
