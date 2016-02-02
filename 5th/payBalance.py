import os
import math

ls = os.linesep

balance = float(raw_input('Enter opening balance: '))
payment = float(raw_input('Enter monthly payment: '))

print ' '*10, 'Amount Remaining', ls
print 'Pymt#', '\t', 'Paid', ' \t'*2, 'Balance', ls
print '-'*5, '\t', '-'*5, '\t'*2, '-'*8

num = int(math.ceil(balance/payment))

for i in range(num):
    residue = balance - payment * i
    if residue < payment:
        print i, '\t', '$%.2f' % residue, '\t'*2, '$0'
    else:
        print i, '\t', '$%.2f' % payment, '\t'*2, '$%.2f' % (balance - payment * i)


    
    
