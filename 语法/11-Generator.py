# yield next() iter()
"""Create a generator that generates the squares of numbers up to some number N."""
# def gensquares(N):
#     for num in range(N):
#         yield (num**2)
# for x in gensquares(10):
#     print(x)
"""Create a generator that yields "n" random numbers between a low and high number (that are inputs)."""
# import random
# def rand_num(low,high,n):
#     for x in range(n):
#         yield random.randint(low,high)
# my_list=[]
# for num in rand_num(1,10,12):
#     my_list.append(num)
# print(my_list)
# gencomp=(item for item in my_list if item>5)
# print(list(gencomp))