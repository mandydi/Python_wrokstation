# class Cylinder:
#
#     def __init__(self, height, radius):
#         self.h=height
#         self.r=radius
#
#     def volume(self):
#         return self.h*self.r*self.r*3.14
#
#     def surface_area(self):
#         return (self.r*self.r*3.14)*2+(2*3.14*self.r*self.h)
#
# c = Cylinder(2,3)
# print(c.volume())
# print(c.surface_area())

class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def __str__(self):
        return f'Account owner: {self.name}\nAccount balance:${self.balance}'
    def deposit(self,num):
        self.balance+=num
        print("Deposit Accepted")
    def withdraw(self,num):
        if num>self.balance:
            print("Funds Unavailable")
        else:
            self.balance-=num
            print("Withdraw Accepted")

acct1 = Account('Jose',100)
print(acct1)
print(acct1.name)
print(acct1.balance)
print(acct1.withdraw(500))