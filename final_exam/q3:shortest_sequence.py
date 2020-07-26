'''what is the legth of the shortest sequence in the file'''

from Bio import SeqIO


min_len = 4894
min_description = ""

f=open("dna2.fasta")

for record in SeqIO.parse('dna2.fasta', "fasta"):
        if len(record) < min_len:
            min_len = len(record)
            min_description = record.description

print(min_description)
print(min_len)
