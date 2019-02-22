import collatz_functions as cf
def makepath(dstart,cstart,pattern,reps):
 print(pattern)
alphabet = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmno pqrstuvwxyz'
# fopen('pathmade.lst', WRITE,TEXT)
coeff = dstart
oldcoeff = coeff/3
const = cstart
print('coeff %d const %d oldcoeff %d' % (coeff,const,oldcoeff))
for i in xrange(1,reps+1):
 print('i',i)
 for j in xrange(1,len(pattern)):
  print('j',j)
  currstep = alphabet.index(pattern[j])
  print('currstep',currstep)
  while currstep>2:
    coeff = 4 * coeff
    const = 4 * const
    currstep = currstep - 2
    print('coeff %d const %d currstep %d' % (coeff,const,currstep))
# if currstep==1:
