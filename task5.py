#Q 1_6
name=input("Enter Your Name")
age=input("Enter Your Age")
street=input("Enter Your Street")
city=input("Enter Your City")
country=input("Enter Your Country")
print(f'"Name : {name}"' )
print(f'"age : {age}"')
new_age=int(age)-5
print(f'"Address : {street},{city},{country}"')
print(f'"Hello {name} Your age is {new_age} Years old,Your Address is{street}, {city}, {country}."')
print(type(name),type(age))
print(type(street),type(city),type(country))
print(f'"Hello {name},How Are You ? \\"Your age is"{new_age}"+ And Your Countre is : {country}')
print(f'''Hello'{name}',How Are You ? \\
\\"Your age is"{new_age}"+And
Your City is :{city}''')
#Q 7_8
name='ITF Gsg python'
print(f'First Letter Is "{name[0]}" ')
print(f'First Letter Is "{name[2]}" ')
print(f'First Letter Is "{name[-1]}" ')
print(name[-3:])
print(name[0:3])
print(name[0:7:2])
print(name[-1:-7:-1])
#Q 9
name="$&$Mohammed$&$&"
print(name.strip('$&'))
#Q 10
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7','Love'))
#Q 11_12
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
#Q 13
#title  يقوم بجعل كل اول حرف من كل كلمة حرف كبير
name1='hello gsg'
print(name1.title())
#capitalize يقوم بحعل الحرف الاول من الكلمة حرف كبير فقط
name1='hello gsg'
print(name1.capitalize())
#Q 14
first_name = "Dana"
print('***********'+first_name)
print('***********'+first_name+'***********')
print(first_name+'***********')
#Q 15
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
#Q 16
print(name_one.isupper())
print(name_two.islower())
#Q 17
print(name_one.startswith("S"))
print(name_two.endswith("HD"))
#Q 18
msg = "I Love Python And Although I Love GSG with Zakaria"
print(msg.count("Love"))
print(msg.count("t"))
#Q 19
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love",1))
#Q 20
def is_symmetrical(input_str):
    cleaned_str = ''.join(filter(lambda x: x.isalnum(), input_str))
    return cleaned_str == cleaned_str[::-1]

def is_palindrome(input_str):
    cleaned_str = ''.join(filter(lambda x: x.isalnum(), input_str))
    return cleaned_str.lower() == cleaned_str[::-1].lower()

test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa."
test4 = "madam"

# Check test1
if is_symmetrical(test1):
    symmetrical_result = "is symmetrical"
else:
    symmetrical_result = "is NOT symmetrical"

if is_palindrome(test1):
    palindrome_result = "is a palindrome."
else:
    palindrome_result = "is NOT a palindrome."

print(f"{test1} {symmetrical_result}, but {test1} {palindrome_result}")
print("################################")

# Check test2
if is_symmetrical(test2):
    symmetrical_result = "is symmetrical"
else:
    symmetrical_result = "is NOT symmetrical"

if is_palindrome(test2):
    palindrome_result = "is a palindrome."
else:
    palindrome_result = "is NOT a palindrome."

print(f"{test2} {symmetrical_result}, and {test2} {palindrome_result}")
print("################################")

# Check test3
if is_symmetrical(test3):
    symmetrical_result = "is symmetrical"
else:
    symmetrical_result = "is NOT symmetrical"

if is_palindrome(test3):
    palindrome_result = "is a palindrome."
else:
    palindrome_result = "is NOT a palindrome."

print(f"{test3} {symmetrical_result}, but {test3} {palindrome_result}")
print("################################")

# Check test4
if is_symmetrical(test4):
    symmetrical_result = "is symmetrical"
else:
    symmetrical_result = "is NOT symmetrical"

if is_palindrome(test4):
    palindrome_result = "is a palindrome."
else:
    palindrome_result = "is NOT a palindrome."

print(f"{test4} {symmetrical_result}, but {test4} {palindrome_result}")
print("################################")