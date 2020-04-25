print('\033c')

# name = input('Enter your name:')
# age = int(input('Enter your age:'))
# print(name)
# print(age+5)

user = input('Enter name: ')
pwd = input('Enter pass: ')

set_user = 'admin'
set_pwd = '1234'

if(user == set_user and pwd == set_pwd):
    print('Login success')
else:
    print('Login fail')
