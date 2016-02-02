numstr = raw_input(' Enter a series of numbers: ')

numseq = list(numstr)

numlen = len(numseq)

for i in range(numlen):
    numseq[i] = int(numseq[i])

numseq.sort(reverse = True)

print numseq
