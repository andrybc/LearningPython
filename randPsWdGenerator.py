import random

#random password generator that must include 1 upercase, a number, and 
#and a special character and then shuffle them all.

char1 = chr(random.randint(65,90))
num1 = chr(random.randint(48,57))
spec1 = chr(random.randint(33,47))

randPass = char1+spec1+num1

print (randPass)

ans = "yes"

while ans == "yes":
    ans = str(input("Do you want to shuffle, yes or no?: "))

    if ans == "yes":
        shrandPass = ''.join(random.sample(randPass,len(randPass)))
        print(shrandPass)
