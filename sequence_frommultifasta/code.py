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
        name=words[0][1:]
        seqs[name]=''
    else:
        seqs[name]=seqs[name]+line

for name,seq in seqs.items():
    print(name,seq)
