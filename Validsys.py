print('Enter your First Name')
firstName = input()
while len(firstName) < 2:
    print('Enter your First Name')
    firstName = input()

print('Enter your Last Name')
lastName = input()
while len(firstName) < 2:
    print('Enter your Last Name')
    lastName = input()

print('Enter your email address')
email = input()
while len(email) < 5:
    print('Enter your email address')
    email = input()
password = input('Enter yes or no: ')
if password == "yes":
    password = firstName[0:2] + lastName[2:]
elif password == "no":
    password = input()
while len(password) < 7:
    print('Enter your password')
    password = input()
print('do you want to use' + firstName[0:2] + lastName[2:] + 'as password')
Container = firstName + lastName + email + password
print("Your User details is" + Container)
