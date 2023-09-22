
# from collections import Counter
# arr = [5, 3, 4, 3, 5, 5, 3]
# c=Counter(arr)
# print(c.most_common())
# print(c.most_common()[:-2-1:-1])
# c.most_common()返回一个列表，包含出现元素及次数，从高到低，倒数的话就是出现次数最少的元素，-n-1是从后往前数第N+1个

# from collections import defaultdict
# d=defaultdict(lambda :0)
# print(d['one'])
# # 它是一个类似于字典的容器，可以用来处理缺失的键。defaultdict有一个参数叫做default_factory，它是一个函数，用来返回缺失键的默认值。您的代码中，您使用了0作为default_factory的参数，但这是不正确的，因为0不是一个函数。当您尝试访问一个不存在的键时，defaultdict会调用default_factory函数，并将其返回值作为键的值。如果default_factory不是一个函数，那么会抛出TypeError异常。所以，您需要使用一个返回0的函数作为default_factory的参数，例如lambda: 0。这样，当您访问一个不存在的键时，defaultdict会调用lambda: 0函数，并将其返回值0作为键的值

from collections import namedtuple
Dog=namedtuple('Dog',['age','breed'])
sam=Dog(age=12,breed='Shepard')