a = raw_input('Enter first num:')
b = raw_input('Enter second num:')
c = raw_input('Enter third num:')
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print'%d %d %d' % (int(a),int(b),int(c))
