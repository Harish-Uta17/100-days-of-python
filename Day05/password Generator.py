import random
letters = ['a','b','c','d','e','f','g','h','i','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3,','4','5','6','7','8','9']
symbols = ['!','@','#','$','&','*','(',')','-','+']

print("Welcome to the pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How manny symbols would you like?\n"))
# easy level
password = ""
# for char in range(0,nr_letters):
#     password += random.choice(letters)
#
# for char in range(0,nr_numbers):
#     password += random.choice(numbers)
#
# for char in range(0,nr_symbols):
#     password += random.choice(symbols)


# Hard level
password_list = []
for char in range(0,nr_letters):
    password_list+= random.choice(letters)

for char in range(0,nr_numbers):
    password_list += random.choice(numbers)

for char in range(0,nr_symbols):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

for char in password_list:
    password += char

print(f"Your password is : {password}")