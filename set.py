print('\x1bc')
# print('\033c')
print(chr(27)+'[2j')

number = {1, 1, 2, 3, 5, 8}

i = 1
while i <= 10:
    print(number, end='\n')
    i = i+1
