print('\x1bc')
# print('\033c')
print(chr(27)+'[2j')

scores = {
    'Alpha': 1200,
    'Beta': 2000,
    'Celta': 4200,
    'Beta': 1200,
}

print(scores)
print(scores['Beta'])

# เพิ่มสมาชิกใหม่เข้า Dictionary
scores['Echo'] = 3200
print(scores)

# การสร้าง Dictionary ว่าง
points = {}

# เพิ่มต่าเข้า Dictionary ว่าง
points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8
print(points)

# การ Loop อ่านสมาชิกของ Dictionary ออกมา
for k, v in scores.items():
    print(k, v)
