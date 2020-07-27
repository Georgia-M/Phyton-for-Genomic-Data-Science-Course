""" Find all repeats of length 12 in the input file.
Let's use Max to specify the number of copies of the most frequent
repeat of length 12. How many different 12-base sequences occur Max times?
"""

f = open("dna2.fasta", "r")
file = f.readlines()

sequences = []
seq = ""
for line in file:
    if not line[0]=='>':
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        seq = seq + line
    else:
        sequences.append(seq)
        seq = ""

sequences.append(seq)

sequences = sequences[1:]

def get_all_repeats(sequence):
    length = len(sequence)
    repeats = []
    for i in range(length):
        repeats.append(sequence[i:i + 12])
    return repeats

all_twelve_repeats = []
for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        if len(j) == 12:
            all_twelve_repeats.append(j)

#find the most frequent sequence
def most_common(lst):
    return max(set(lst), key=lst.count)

#find how many times the most frequent occurs
no_max=all_twelve_repeats.count(most_common(all_twelve_repeats))
#print(no_max)

#find how many different sequences occur no_max times
different_list = []
k=0
for i in all_twelve_repeats:
    if i.count(most_common(i))==no_max:
        k+=1
print(k)
