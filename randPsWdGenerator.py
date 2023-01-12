import random

#random password generator that must include 1 upercase, a number, and 
#and a special character and then shuffle them all.

uchar1 = chr(random.randint(65,90))
num1 = chr(random.randint(48,57))
num2 = chr(random.randint(48,57))
spec1 = chr(random.randint(33,47))
lchar1 = chr(random.randint(97,122))
lchar1 = chr(random.randint(97,122))
lchar2 = chr(random.randint(97,122))
lchar3 = chr(random.randint(97,122))


randPass = uchar1+spec1+num1+num2+lchar1+lchar2+lchar3

print (randPass)

shuffle = "yes"

while shuffle == "yes":
    shuffle = str(input("Do you want to shuffle, yes or no?: "))

    if shuffle == "yes":
        shrandPass = ''.join(random.sample(randPass,len(randPass)))
        print(shrandPass)
