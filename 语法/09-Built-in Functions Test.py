"""pro 1 """
# def word_lengths(phrase):
#     return list(map(len,phrase.split()))
# #这里len不带括号parentheses是将len函数应用于split()返回的单词列表的每个单词
# print(word_lengths('How long are the words in this phrase'))

# from functools import reduce
# def digits_to_num(digits):
#     return reduce(lambda x,y:x*10+y,digits)
# print(digits_to_num([3,4,3,2,1]))
"""problem 3"""
# def filter_words(word_list,letter):
#     return list(filter(lambda x:x[0]==letter,word_list))
# l = ['hello','are','cat','dog','ham','hi','go','to','heart']
# print(filter_words(l,'h'))
"""problem 4"""
# def concatenate(L1, L2, connector):
#     output=[]
#     for str1,str2 in zip(L1,L2):
#         output.append(str1+connector+str2)
#     return output
# print(concatenate(['A','B'],['a','b'],'-'))
# zip对列表的重组，列表的元素添加
"""problem 5"""
# def d_list(L):
#     return {num:item for item,num in enumerate(L)}
# # enumerate()遍历对象返回（索引，元素）
# #如何构建返回一个字典
# print(d_list(['a','b','c']))
"""problem 6"""
# def count_match_index(L):
#     return len([item for count,item in enumerate(L) if count==int(item)])
# print(count_match_index([0,2,2,1,5,5,6,10]))
# 返回一个字典一个列表 [num for num in enumerate(iterable)]