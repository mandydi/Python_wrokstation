"""Write a function that computes the volume of a sphere given its radius."""
def vol(rad):
    return 4.0/3*rad*rad*rad*3.14
print(vol(2))

"""Write a function that checks whether a number is in a given range (inclusive of high and low)"""
def ran_check(num,low,high):
    if num <= low and num >= high:
        return True
    else:
        return False

"""Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters."""
def up_low(text):
    up_num=0
    low_num=0
    for ch in text:
        if ch.isupper():
            up_num+=1
        elif ch.islower():
            low_num+=1
        else:
            pass
    print('upper case ch:{}'.format(up_num))
    print('lower case ch:{}'.format(low_num))
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

"""Write a Python function that takes a list and returns a new list with unique elements of the first list."""
def unique_list(lst):
    return  set(lst)
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
"""Write a Python function to multiply all the numbers in a list."""
"""Write a Python function to multiply all the numbers in a list."""
"""Write a Python function that checks whether a word or phrase is palindrome or not."""
def palindrome(s):
    lst=s[::-1]
    if lst==s:
        return True
    else:
        return False
print(palindrome('nurses run'))
