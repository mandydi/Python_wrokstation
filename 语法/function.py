# even_list=[]
# def check_even(num_list):
# 	for num in num_list:
# 		if num % 2 == 0:
# 			even_list.append(num)
# 	return False
# list01=[1,2,4,3,4,5]
# check_even(list01)
# print(set(even_list))

# from random import shuffle
# """"how to shuffle a list"""
#
# def suffle_list(list):
# 	shuffle(list)
# 	return list
# def guess_game():
# 	guess=''
# 	while guess not in ['0','1','2']:
# 		guess=input("imput your guess num")
# 	return int(guess)
# def check_guess(g_num,g_list):
# 	if g_list[g_num] == 'O':
# 		print('great job!')
# 	else:
# 		print('wrong!')
# 		print(g_list)
#
# ori_list=[' ','O',' ']
# guess=guess_game()
# print(guess)
# mix_list=suffle_list(ori_list)
# check_guess(guess,mix_list)

"""LESSER OF TWO EVENS"""
# 分为比较大小和是否偶数，我卡在先比大小需要比两次，考虑到都是奇数的情况
# def lesser_of_two_evens(num1,num2):
    # m_num=num1
    # if num2>num1:
    #     m_num=num2
    #     if m_num%2==0:
    #         return m_num
    #     else:
    #         pass
    # else:
    #     if m_num%2==0:
    #         return m_num
    #     else:
    #         pass
"""ANIMAL CRACKERS"""
def animal_crackers(str):
    # 形参可不带类型，怎么知道str是个迭代对象
    wordlist=str.split()
    return wordlist[0][0]==wordlist[1][0]

"""MAKES TWENTY"""
def makes_twenty(num1,num2):
    sum=num1+num2
    if sum or num1 or num2 == 20:
        return  True
    else:
        return  False
"""OLD MACDONALD"""
def old_macdonld(name):
    if len(name)>3:
        return name[:3].capitalize()+name[3:].capitalize()
    else:
        print("name is too short")

"""REVERSED SENTENCE"""
def reversed(str):
    return ' '.join(str.split()[::-1])
"""Within ten of either 100 or 200"""
def almost_there(num):
    if abs(num-100) or abs(num-200) <= 10:
        return True
    else:
        False
"""find 33"""
def find33(num_list):
    count = 0
    for num in num_list:
        if num == 3:
            count+=1
        else:
            count=0
    if count>=2:
        return True
    else:
        return False
"""paper Doll"""
def paper_doll(word):
    dst_str=''
    for letter in word:
        dst_str+=letter*3
    return dst_str
"""BlackJack->21."""
def BlackJack(n1,n2,n3):
    nums=[n1,n2,n3]
    result=0
    count=0
    for num in nums:
        if num > 1 and num <= 11:
            result+=num
        else:
            print("num out of range")
        if num ==11:
            count+=1
        else:
            pass
    if result>21 and count==1:
        result-=10
        return  result
    elif result >21:
        print("BUST")
    else:
        return result
"""except section of 69"""
def summer_69(num_list):
    summer_69_result=0
    add=True
    for num in num_list:
        while add:
            if num != 6:
                summer_69_result+=num
            else:
                add=False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return  summer_69_result
"""Spy game"""
def spy_game(num_list):
    spy_game_sum=0
    for i in enumerate(num_list):
        if num_list[i] == 0:
            spy_game_sum=spy_game_sum+num_list[i+1]+num_list[i+2]
        else:
            pass
    if spy_game_sum==7:
        return True
    else:
        return False
"""spy game right"""
def spy_game(nums):
    code = [0, 0, 7, 'x']  #in order

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1