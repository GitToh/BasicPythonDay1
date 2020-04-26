# แสดงภาษาไทย
print('\033c')

# i = 1
# while i <= 10:
#     if i == 10:
#         print(i)
#     else:
#         print(i, end=',')
#     i = i+1

a = 1
# while a <= 10:
#     print(a)
#     a = a+1

i = 1
while i <= 90:
    # t = i % 2 == 0 and 'คู่' or 'คี่'
    # t = 'คู่' if i % 2 == 0 else 'คี่'
    t = ('คี่', 'คู่')[i % 2 == 0]
    if i % 10 == 0:
        print(f'{i}[{t}]', end='\n')
    else:
        print(f'{i}[{t}]', end=',')
    i = i + 1

print('\n')


a, b = 10, 10
print(f"{(('b>a', 'a>b')[a > b], 'a==b')[a == b]}")


x = 0
a = (1, 0)[x == 0]
b = 0 if x == 0 else 1
c = x == 1 and 1 or 0
print(a)
print(b)
print(c)
