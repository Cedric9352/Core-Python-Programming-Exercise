a = raw_input('Please enter an number between 0 and 100: ')
amount = int(a)
count = 100
oa = fa = ta = tfa = 0

for one in range(101):
    for five in range(21):
        for ten in range(11):
            for twenty_five in range(5):
                if ((one * 1)+(five * 5)+(ten * 10)+(twenty_five * 25) == amount) and \
                  ((one + five + ten + twenty_five) < count):
                    count = one + five + ten + twenty_five
                    oa = one
                    fa = five
                    ta = ten
                    tfa = twenty_five
print "%d one %d five %d ten %d twenty_five" % (oa,fa,ta,tfa)
