print('\x1bc')
# print('\033c')
print(chr(27)+'[2j')

number = (1, 1, 2, 3, 5, 8)
mixed = (12, 20, [5, 4, 3], True, 'Samit')

print(number[2])
print(mixed[1])
print(mixed[2])
print(mixed[2][1])

# ลองเปลี่ยนแปลงค่าสามาชิก
number[2] = 10
print(number)
