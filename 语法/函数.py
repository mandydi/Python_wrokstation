#创建函数
def myfun():
    pass
#传递参数
def robot(title,times):
    if times==0:
        print("打印次数为0")
    else:
        for i in range(times):
            print(f"I LOVE {title}")
robot("unni",5)
#默认返回值为NONE
print(f"默认返回值{myfun()}")
#位置参数，默认参数，关键字参数
#*之后都要用关键字参数，只能在位置参数之后
def myfunc(a,*,b,c):
    print(a,b,c)
myfunc(10,b=5,c=0)
#解包参数
args=(164,62,10,00)
def myfund(a,b,c,d):
    print(a,b,c,d)
myfund(*args)
kwargs={'a':164,'b':62,'c':10,'d':00}
myfund(**kwargs)
#作用域，变量名相同局部变量进行覆盖
static_x=880
def myfune():
    x=520
    print(x)
myfune()
#global
#nonlocal
#LEG B
#闭包：嵌套函数的外层作用域具有记忆能力，将内层函数作为返回值返回
def power(exp):
    def result(base):
        return base**exp
    return  result
square=power(2)
re=square(2)
print(re)
#装饰器
import  time
def logger(msg):
    def time_master(func):
        @functools.wraps(func)
        def call_func():
            start=time.time()
            func()
            stop=time.time()
            print(f"{msg}耗时{(stop-start):.2f}秒")
        #返回函数名
        return call_func
    return time_master

#给装饰器传递参数
@logger(msg="A")
def myfunf():
    time.sleep(2)
    print("正在调用函数")

myfunf()
#如果不用装饰器
myfunf=logger(msg="B")(myfunf)
#为什么会先输出A在输出B
myfunf()
#lamba
#生成器不支持下标
def fib():
    back1,back2=0,1
    while True:
        yield  back1
        back1,back2=back2,back1+back2
f=fib()
for i in f:
    print(i)
    if i>=1000:
        break
#递归
#递归求阶乘
def fung(i):
    if i == 1:
        return 1
    else:
        return i*fung(i-1)
print(fung(3))
#递归求斐波那契数列
def funh(i):
    if i == 1 or i==2:
        return 1
    else:
        return funh(i-1)+funh(i-2)
print(funh(12))
def funi(n):
    a=1
    b=1
    c=1
    while n>2:
        c=a+b
        a=b
        b=c
        n-=1
    return c
print(funi(120))
#汉诺塔问题 f(n+!)=2*f(n)+1
def hanoi(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y)
        print(x,"-->",z)
        hanoi(n-1,y,x,z)
n=int(input('input your floor num:'))
hanoi(n,'a','b','c')
#函数文档
#类型注释
#内省
#高阶函数 以函数作为参数
def  add(x,y):
    return x+y
import functools
print(functools.reduce(add,[1,2,3,4,5]))
#1到10的阶乘
print(functools.reduce(lambda x,y:x*y,range(1,11)))
#偏函数
#@wrap 还原闭包真正调用的函数