# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except:
#     print("unsupported operand type(s) for ** or pow(): 'str' and 'int'")
def ask():
    while True:
        try:
            val=input("please input your int")
        except:
            print("An error occurred!Please try again")
            continue
        else:
            print(f'Thank you,your number squared is:{val}')
            break
ask()