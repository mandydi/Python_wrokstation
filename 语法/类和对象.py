#类=对象+方法
#可以给对象添加属性
#self参数是实例化对象本身
#继承
class A:
    id={"name":"显示器","tall":158}
    def say(self):
        print("现在可以设置我的比例")
class B:
    id={"name":"地主","tall":178}
    buff="大爹没有B才会接着往下找"
    def say(self):
        print("我是新来的B")
class C(A,B):
    i1=A()
    i2=B()
    def say(self):
        self.i1.say()
        self.i2.say()
c=C()
print(c.buff)
#多重继承集合
c.say()
#__dict__进行内省
#可以通过类名.成员修改属性，因为这个类是一个预制对象
class D:
    pass
D.x=100
#构造
#重写
#使用super()自动搜寻父类的相关方法并且避免重复调用
class B0:
    def __init__(self):
        print("我是B0")
class B1(B0):
    def __init__(self):
        #没有super不会打印b0和b2
        super().__init__()
        print("我是B1")
class B2(B0):
    #01子类一定需要初始化吗？如果没有super，不会打印B0
    def __init__(self):
        super().__init__()
        print("我是B2")
class B3(B1,B2):
    def __init__(self):
        super().__init__()
        print("我是B3")
b3=B3()
#Mix-in
#Aniaml相当于工厂,从这个工厂生产的实例有共同声明say，独立标签，还可以返工添加插件Mixin
class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say(self):
        print(f"i am {self.name},age is {self.age}")
class SwimMixin:
    def swim(self):
        print("我还会swim，你在照镜子吗？")
class Pig(SwimMixin,Animal):
    def special(self):
        print("我会供大白菜")
p=Pig("edda","25")
#p.say()
p.swim()
p.special()
#多态:体现了面向对象，并不是通过传入参数不同而执行不同动作
class Cat(Animal):
    def special(self):
        print("小喵咪也有两面,都给我吧")
#只要x里面有say()就不会报错
def Factory(x):
    x.say()
c=Cat("cindy",27)
Factory(p)
Factory(c)
#鸭子模型,并没有出厂声明
class Duck():
    def say(self):
        print("我也想被富婆包养")
d=Duck()
Factory(d)
#私友变量
class Rabbit:
    def __init__(self,key,func):
        self.__x=key
        self.func=func
    def setx(self,key):
        self.__x=key
    def getx(self):
        print(f"插入{self.__x}从后面进来，记得关门")
    def __del__(self):
        self.func(self)

#python回收站
def Hookk():
    x=0
    def inner(y=None):
        nonlocal x
        if y:
            x=y
        else:
            return x
    return inner
f=Hookk()
r01=Rabbit(1200,f)
r01.getx()
#名字改编是发生在类实例化时期
r01.__y=300
r01.__dict__
r01.__dict__['z']=880
#在实例摧毁之前进行拷贝
del r01
r2=f()
r2.getx()
#属性访问
#索引切片
class Double:
    def __init__(self,start,stop):
        self.value=start-1
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value==self.stop:
            raise StopIteration
        self.value+=1
        return self.value*2
d=Double(1,5)
for i in d:
    print(i,end="\n")
#property函数来只读存储删除变量，避免意外事件
#classmath类方法 统计继承中各个类的实例对象
class LeiC:
    count=0
    @classmethod
    def add(cls):
        cls.count+=1
    def __init__(self):
        self.add()
    @classmethod
    def get_count(cls):
        print(f"该类一共实例化{cls.count}个对象")
class LeiD(LeiC):
    pass
class LeiE(LeiC):
    pass
#静态方法
class StaC:
    count=0
    def __init__(self):
        StaC.count+=1
        #不会因为属性被覆盖受影响
        @classmethod
        def get_count():
            print(f"该类一共创建了{StaC.count}个对象")