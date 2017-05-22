# coding: latin-1
#
# http://hplgit.github.io/bioinf-py/doc/pub/bioinf-py.html
for c in 'ATGC':
    print c

def count_v6(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        m.append(True if c == base else False)
    return sum(m)

dna = 'ATTTGCCATGCCC'

print 'Count:'+str(count_v6(dna,'A'))

def count_v9(dna, base):
    return sum([c == base for c in dna])

print 'Count:'+str(count_v9(dna,'B'))

N = 12
dna = 'A'*N

import random
alphabet = list('ATGC')
dna = [random.choice(alphabet) for i in range(N)]
dna = ''.join(dna)  # join the list elements to a string

print alphabet

print dna
