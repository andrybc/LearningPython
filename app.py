
# print('Andry Canel')
# print('o----')
# print(' ||||')
# print('L' * 20)
# price = 100
# print(price)
print("Welcome to Florida Hospital! Please sign in the patient on our clipboard")
last_name = input("Last Name: ")
first_name = input("First Name: ")
sex = input("Sex: M(male) or F(female): ")
DOB = input("Birthdate: ")
phoneNum = int(input("Cell: "))
is_Emergency = bool(input("Is this an emergency? True or False:"))

if sex == 'M':
    print(f"Good morning Mr. {last_name}")
else:
    print(f"Good morning Ms. {last_name}")

print(f"Your date of birth is {DOB}. And we can contact you at { phoneNum}")
if is_Emergency:
    print("""You stated this is an emergency so can you please tell me what the situation is so we can help
          you right away""")
    emergency_notes = input("...: ")
else:
    print("""Since this is not an emergency can you please wait in the lobby area until you hear your name called. 
          thank you for your patience""")

birthyear = int(DOB[-4:])
print(birthyear)
age = 2022 - birthyear
print(age)

weight_lbs = float(input("Weight (lbs"))
weight_kgs = weight_lbs * 0.45
print(weight_kgs)