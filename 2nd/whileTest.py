while True:
    i = raw_input('Enter a number:')
    if int(i) % 7 ==0:
        print 'Entered successfully'
        break
    else:
        print 'Please enter again!'
