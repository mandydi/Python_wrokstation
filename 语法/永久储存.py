f=open("unni.txt","w")
f.writelines(["this is a test\n i am an ai"])
f.close()
#以w+打开不操作会清空
f=open("unni.txt","w+")
f.close()
f=open("unni.txt","r+")
f.read()
#建议使用a+权限不会清空

#with 上下文可以解决资源释放问题
with open("unni.txt","a+") as f:
    f.write("\nwith style make true")
#pickle 二进制io
import pickle
a="unni"
b=23
c={"tall":164,"weig":62,"len":10}
with open("ident.pkl","wb") as f:
    pickle.dump((a,b,c),f)

with open("ident.pkl","rb") as f:
    a,b,c=pickle.load(f)
print(a,b,c,sep="\n")

#异常处理
try:
    1/0
    520+"unni"
except ZeroDivisionError as e:
    print(e)
except ValueError as v:
    print(v)
#执行到1/0就直接跳转处理异常，可以同时处理多个异常，不匹配也会爆红
#else是没有触发异常执行的代码
#finally无论有没有异常都会进行收尾工作
#嵌套异常
#raise语句 用于自爆，不能生成不存在的错误
try:
    1/0
except:
    raise ValueError("你这可不行") from ZeroDivisionError
#assert
#利用raise实现goto
# try:
#     while True:
#         for i in range(10):
#             if i > 3:
#                 raise
#             print(i)
# except:
#     print("goto到这里来")