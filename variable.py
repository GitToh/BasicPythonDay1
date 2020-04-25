a = 3
b = 3.14
c = 'IT GENIUS'

print(a)
print(b)
print(c)

print(a, b, c)

# ตัวแปรหลายบรรทัด
x = y = z = 10
j, k = 5, 15
print(x, y, z)
print(j, k)

# Boolean
status = True
msg = False
print(status, msg)

# แสดงตัวแปรในข้อความ วิธีที่1 concat string
print('ราคาขายต่อชิ้น', b, 'บาท มีจำนวน', a, 'ชิ้น')

# แสดงตัวแปรในข้อความ วิธีที่2 string interpolation
print('ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น' % (b, a))

# แสดงตัวแปรในข้อความ วิธีที่3 format string
print(f'ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น')
