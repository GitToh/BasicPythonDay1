import sys
print(sys.stdout.encoding)  # should be utf8

print(f'sys default encoding is  {sys.getdefaultencoding()}')
print(f'stdout encoding is {sys.stdout.encoding}')
print('printing eggplant emoji: 🍆')
exec('print("🍆")')
