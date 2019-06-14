# 欢迎来到西瓜籽的肚子里
这是小火车用python写的一个接在酷Q的机器人，之后会慢慢解释
## 一、西瓜是什么
是一个用于新生群做咨询和聊天的机器人，日常词库用于回答新生的一些基础问题，还有就是查询每日的实时天气(之后也会详细讲)
## 二、西瓜的原理是什么
1. 酷Q Air版是本体 [酷Q-Air官网](https://cqp.cc/t/23253)
2. CQhttp是酷Q能开发python或者其他版本聊天bot的关键 [Github上的搜索结果](https://github.com/search?q=cqhttp)
3. [CQhttp-python](https://github.com/richardchien/python-cqhttp)  CQhttp的python版
4. [nonebot](https://github.com/richardchien/nonebot):基于 酷Q 的 Python 异步 QQ 机器人框架 [基础教程](https://none.rclab.tk/) [进阶API](https://none.rclab.tk/api.html)

## 三、西瓜的插件
因为nonebot本身支持插件，所以我就写了三个插件

### 1.天气插件
以前我用的是[天气API](https://www.tianqiapi.com/)这个网站，但是吧，搜台湾搜不到，emmmmmmm在我发现这件事的第二天网站就停了，然后恢复了之后还是没有台湾，我不喜欢它了

现在我用的是[和风天气](https://www.heweather.com/),免费用户支持三个小时内的实况天气，也很详细，支持精确到大部分地区，比如中国广东湛江霞山，但是不支持直接搜索广东这种省级城市，支持数百个热门海外城市

### 2.群管理
就是自动同意加群和欢迎新来的而已

### 3.自动回复
这一块可能是我做的最多的了，重点都在词库(res文件夹)里，Q.json是问题的关键字，A.json是答案


## 四、西瓜的实现
1. 酷Q在windows上(或者在docker里)运行
2. 安装cqhppt的应用到酷Q并配置好配置文件
3. 在有python3的Windows或者Linux环境上运行nonebot
4. 成功将nonebot和cqhttp相连，任务结束