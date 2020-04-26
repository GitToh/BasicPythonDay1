from Car import*

print('\x1bc')
# print('\033c')
print(chr(27)+'[2j')

# สร้าง Object หรือ Instance ของ Class car
objcar1 = Car('red', 'Toyota', 4, 4, 180)
objcar1.printdata()

print()

objcar2 = Car
# objcar2.setbrand = 'Honda'
# objcar2.setbrand = 'Yellow'
# objcar2.setspeed = '200'
objcar2.printdata()
