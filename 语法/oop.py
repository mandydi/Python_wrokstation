# #继承
# class A:
#     def __init__(self):
#         print("A is created")
#     def action(self):
#         print("A test inhrentance")
# class B(A):
#     def __init__(self):
#         print("B is created")
#     # def action(self):
#     #     self.a=A()
#     #     self.a.action()
#     #     print("B can walk")
#
# #多态
# class C(A):
#     def __init__(self):
#         print("C is created")
#     def action(self):
#         print("C can swim")
#
# b=B()
# b.action()
# """"b.action()突出继承原理，b类里面没有action方法，可是A类里面有action"""
# c=C()
# c.action()
# """c.action突出多态原理，不同对象引用相同方法名来进行多态"""

class Chips:
    def __init__(self):
        self.bet=0
        self.total=100
    def win_bet(self):
        self.total-=self.bet
    def lose_bet(self):
        self.total+=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("please input your bet"))
        except ValueError:
            print("please input integer")
        else:
            if chips.bet>chips.total:
                print("you don't have the number of total for your bet")
            else:
                break

test_chips=Chips()
take_bet(test_chips)
print(test_chips.bet)

# 这个例子我其实想记录take_bet传进来的参数，有这么多个提前定义好的类，他怎么就知道我传进来的是什么类型
#所以面向对象打点根本没有提示