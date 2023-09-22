from functools import reduce
#Map funcation:make sure understand for multiple iterable item
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
"""map()"""
# d=list(map(lambda x,y,z:x+y+z,a,b,c))
"""reduce()"""
# find_max=lambda x,y:x if (x>y) else y
# d=reduce(find_max,[a,b,c])
"""filter()"""
# d=list(filter(lambda x:x%2==0,range(20)))
"""zip()"""
# d1={'a':1,'b':2}
# d2={'c':4,'d':5}
# def switch(d1,d2):
#     dout={}
#     for d1key,d2value in zip(d1,d2.values()):
#         dout[d1key]=d2value
#     return dout
# print(switch(d1,d2))
"""enumerate()"""
# for num,item in enumerate(a):
#     if num >= 2:
#         break
#     else:
#         print(item)
# months=['March','April','May','June']
# print(list(enumerate(months,start=3)))

"""all() and any()"""
"""complex()"""
print(complex(10,1))
