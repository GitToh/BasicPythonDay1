# Import ทั้งหมดทุกฟังก์ชันใน Module
# import numbers

# Import มาบางฟังก์ชัน
# from numbers import factorial, fibonacci

# Import ทุกฟังก์ชัน
# from numbers import *

# Import และเปลี่ยนชื่อฟังก์ชัน (นามแฝง) alias
from numbers import factorial as fa, fibonacci as fi

print('\x1bc')
# print('\033c')
print(chr(27)+'[2j')


# เรียกใช้งาน
# print(f'{numbers.factorial(5)}')
# print(f'{numbers.fibonacci(100)}')

# print(factorial(5))
# print(fibonacci(100))

# เรียกใช้แบบนามแฝง
print(fa(5))
print(fi(100))
