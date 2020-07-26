''' how many records (=how many different sequences) are in the multi-Fasta file?'''

try:
    f=open("dna2.fasta")
except IOError:
    print("the file dna2 does not exist")

seqs={}
i=0

for line in f:
    line=line.strip("\n")
    if line[0]=='>':
        words=line.split()
        i+=1
    
print(i)
