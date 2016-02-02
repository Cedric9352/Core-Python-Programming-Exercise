import string
import keyword

alphas = string.letters + '_'
nums = string.digits
kwlist = keyword.kwlist

print 'Welcome to the Identifier Checher v1.0'
myInput = raw_input(' Enter a identifier to test: ')

if len(myInput) > 0:
    if myInput[0] not in alphas:
        print 'Invalid identifier!'
    elif myInput in kwlist:
        print 'Keywords are not allowed!'
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums :
                print 'Invalid input!'
                break
        else:
            print 'Okey as an identifier'
else:
    print 'Empty input!'
        
                
