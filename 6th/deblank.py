str_input = raw_input('Enter a string: ')

str_list = list(str_input)

while True:
    if(str_list[0] == ' '):
        str_list.pop(0)
    elif(str_list[-1] == ' '):
        str_list.pop()
    else:
        break
    
print ''.join(str_list)
