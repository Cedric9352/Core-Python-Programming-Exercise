import os

while True:
    fname = raw_input('Enter a filename:')

    if os.path.exists(fname):
        fobj = open(fname, 'r')
        for eachLine in fobj:
            print eachLine,
        fobj.close()
        break
    else:
        print "ERROR: File not found!"
