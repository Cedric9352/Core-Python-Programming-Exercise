import os
ls = os.linesep

while True:
    fname = raw_input('Please input a name for file:')
    try:
        fobj = open(fname, 'r')
    except IOError,e:
        break;
    else:
        print "ERROR: '%s' already exists" % fname

all = []
print "\nEnter lines('.' by itself to quit).\n"

while True:
    entry = raw_input('>>>')
    if entry == '.':
        break;
    else:
        all.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'Done!'
        
