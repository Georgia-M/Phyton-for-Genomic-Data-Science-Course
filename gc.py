#!/usr/bin/python

dna = 'acgctcgcgcgcggcgatagctgcagtgtgcataattttgggac'
no_c = dna.count('c')
no_g = dna.count('g')
dna_lenght = len(dna)
gc_percent = (no_c+no_g)*100/dna_lenght
print(no_g, no_c, dna_lenght, gc_percent)


