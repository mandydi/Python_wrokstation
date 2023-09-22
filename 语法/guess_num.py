import random
num=random.randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
gue_num=[0]

while True:
    guess = int(input("please input your guess"))

    if num==guess:
        print("great job!")
        break
    gue_num.append(guess)
    if guess<1 or guess>100:
        print("out of bonus")
        continue
    if gue_num[-2]:
        last_distance=abs(gue_num[-2]-num)
        if abs(guess-num)<last_distance:
            print("WRAMER")
        else:
            print("COLDER!")
    else:
        if abs(guess-num)<10:
            print("wram")
        else:
            print("clod")

