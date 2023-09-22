# #输出10以内的素数
# for n in range(2,11):
#     for x in range(2,n):
#         if n%x==0:
#             print(n,"=",x,"*",n//x)
#             break
#     else:
#         print(n,"this is su shu")


# x={"吕布":"口口布","关羽":"关习习"}
# z=dict(吕布="口口布",关羽="关习习")
# y=dict([("吕布","口口布"),("关羽","关习习")])
# del x["吕布"]
# print(x)
#只有可哈希的对象才能作为字典和集合的元素,那如何实现嵌套集合
# x={1,2,3}
# z=frozenset(x)
# y={z,4,5,6}

import random
import timeit
hastack=[random.randint(1,1000000) for i in range(1000000)]
needles=[random.randint(1,1000) for i in range(1000)]

# 集合背后有散列表支持，查找效率翻倍
hastack=set(hastack)

def find():
    found = 0
    for each in needles:
        if each in hastack:
            found += 1
    print(f"一个找到{found}个匹配")

t=timeit.timeit("find()",setup="from __main__ import find",number=1)
print(f"查找过程一共消耗{t}秒")