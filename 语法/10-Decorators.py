# def hello(name='Jose'):
#     def greet():
#         return '\t This is inside the greet() function'
#
#     def welcome():
#         return "\t This is inside the welcome() function"
#
#     if name == 'Jose':
#         return greet
#     else:
#         return welcome
#
# print(hello(name='SM'))
# 注意他返回的函数没带()，可以作为object传递

def new_hello(func):
    print("hello decorator")
    print(func())
# new_hello(hello)
# 先弄清楚他为什么需要我们明白函数是可以当作对象来传输的
@new_hello
def hello():
    print("testing pass into arugment")

hello()
# 装饰器每次调用这个函数时，就会把这个函数当作参数传递给装饰器所标注的函数