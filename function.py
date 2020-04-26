print('\x1bc')
# print('\033c')
print(chr(27)+'[2j')


# การสร้างฟังก์ชันแบบไม่มีการ Return value
def hello(name='null'):
    print(f'Hello {name}')


# สร้างฟังก์ชั่นแบบมีการ Return value
def area(width, height):
    total = width*height
    return total


# ฟังก์ชันแบบมีค่าเริ่มต้น
def showinfo(name='', salary=0.00, lang='not define'):
    print(f'Name: {name}')
    print(f'Salary: {salary}')
    print(f'Language: {lang}')


# เรียกใช้งานฟังก์ชัน hello()
hello('Samit')

# เรียกใช้งานฟังก์ชัน area()
print(area(5, 8))
print(area(15, 7.8))

# เรียกใช้งานฟังก์ชัน showinfo()
showinfo()
print()
showinfo('Samit', 12000, 'PHP')
