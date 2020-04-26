print('\x1bc')
# print('\033c')
print(chr(27)+'[2j')
number = [1, 1, 2, 3, 5, 8, 13]
name = ['Alpha', 'Beta', 'Celta', 'Echo']
mixed = [10, 25.75, True, 'Samit']

# การเข้าถึงสมาชิกใน List
print(number[1])
print(name[3])
print(mixed[2], mixed[3])

# การนับจำนวนสมาชิกใน List
print(f'สมาชิกทั้งหมดของ Number={len(number)}')

# การสร้าง List แบบว่าง (empty list)
data = []

# การเพิ่มสมาชิกเข้าไปใน List ว่าง
data.append(10)
data.append(15)
data.append(20)
print(data)

# การอัพเดตสมาชิกใน List
data[1] = 12
print(data)

# ฟังก์ช้นวนลูปอ่านสมาชิกทั้งหมด
sum = 0
for num in number:
    sum += num

print(sum)
