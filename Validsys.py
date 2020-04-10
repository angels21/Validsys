import random
import string
import uuid

print('Enter your First Name at least two characters')
firstName = input()
while len(firstName) < 2:
    print('Enter your First Name at least two characters')
    firstName = input()

print('Enter your Last Name at least two characters')
lastName = input()
while len(firstName) < 2:
    print('Enter your Last Name at least two characters')
    lastName = input()

print('Enter your email address at least 5 characters')
email = input()
while len(email) < 5:
    print('Enter your email address at least 5 characters')
    email = input()

id = uuid.uuid1()

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))
randomstring = randomString(5)
print('Do you want to use ' + firstName[0:2] + randomstring + lastName[-2:]+' as password?')
password = input('Enter yes or no: ')
if password == "yes":
    password = (firstName[0:2] + randomstring + lastName[-2:])
    print('Your password is saved in the backend press enter to print your saved details')

    Container = [['First Name', firstName], ['Last Name', lastName], ['Email', email], ['Password', password ], ['uniqueid', id.node]]
    for row in Container:
        print("{: >20} {: >20}".format(*row))

elif password == "no":

    print('Enter your preferred password which must be more than 7 characters')
password = input()
while len(password) < 7:
    print('Enter atleast 7 characters as your password')
    password = input()
Container = [['First Name', firstName], ['Last Name', lastName], ['Email', email], ['Password', password ], ['uniqueid', id.node]]
for row in Container:
                        print("{: >20} {: >20}".format(*row))
