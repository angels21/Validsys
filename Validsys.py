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
print('do you want to use ' + firstName[0:2] + lastName[2:] + ' as password?')
answer = input('Enter yes or no: ')
if answer == "yes":
    password = (firstName[0:2] + lastName[2:])
    print("Your password is saved in the secured backend as *******")
elif answer == "no":

    print('Enter your password')
password = input()
while len(password) < 7:
    print('Enter your password')
    password = input()
Container = firstName + lastName + email + password
print("Your User details is " + Container + " and is now saved in our database")
