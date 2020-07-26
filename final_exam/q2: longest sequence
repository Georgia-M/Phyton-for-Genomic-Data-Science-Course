'''what is the length of the longest sequence in the file'''

from Bio import SeqIO


max_len = 0
max_description = ""

f=open("dna2.fasta")

for record in SeqIO.parse('dna2.fasta', "fasta"):
        if len(record) > max_len:
            max_len = len(record)
            max_description = record.description

print(max_description)
print(max_len)
