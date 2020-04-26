# print(chr(27)+'[2j')
# print('\033c')
print('\x1bc')
print('------------------------------')
print('> Summation Program')
print('> Type \'e\' to exit the program')
print('------------------------------')

# ตัวแปรไว้เก็บผลรวม
sumdata = 0
count = 1

while True:
    data = input(f'Enter number {count}: ')
    # ตรวจสอบผู้ใช้ป้อน 'e'
    if data == 'e':
        break

    # การหาผลรวม
    sumdata += int(data)
    count = count + 1

print(f'Sum value is {sumdata}')
