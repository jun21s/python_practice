# print 사용법
# 파이썬 완전 기초

# 기본 출력
import sys
print(1)
print('this is one')
print("hello")
print('''0''')
print()

# separator 옵션
print('p', 'y', sep='-')
print('010', '0000', '0000', sep='-')
print('python', 'google.com', sep='@')
print()

# end 옵션
print('welcone to', end=' - ')
print('it news', end=' - ')
print('web site')
print()

# file 옵션
print('learn python', file=sys.stdout)
print()

# format 사용(d 정수, s 문자열, f 실수)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' % ('nice111'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice111'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:0>10}'.format('nice'))
print('{:_^10}'.format('nice'))

print('%5s' % ('nice'))
print('%.5s' % ('123456789'))

print('{:10.7}'.format('123456789'))
print()
# %d
print('%d %d' % (1, 2))
print('{}{}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()
# %f
print('%f' % (3.141592))
print('%1.3f' % (3.141592))
print('{:f}'.format(3.141592))

print('%06.3f' % (3.141592))
print('{:06.2f}'.format(3.141592))
