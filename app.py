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
    print("Good morning Mr. "+ last_name)
else:
    print("Good morning Ms. " + last_name)

print("Your date of birth is " + str(DOB) + ". And we can contact you at " + str(phoneNum))
if is_Emergency:
    print("You stated this is an emergency so can you please tell me what the situation is so we can help"
          " you right away")
    emergency_notes = input("...: ")
else:
    print("Since this is not an emergency can you please wait in the lobby area until you hear your name called. "
          "thank you for your patience")



