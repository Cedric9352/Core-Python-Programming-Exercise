filename = raw_input('Enter file name:')
fobj = open(filename, 'r')
for Line in fobj:
    print Line,
fobj.close()
