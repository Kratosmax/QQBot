import re

string = "啊的手本部法首发打发发发发撒空调法"

kw = "(白云.*空调)|(空调.*白云)"

res = re.findall(kw,string)
print(res)
print(len(res))