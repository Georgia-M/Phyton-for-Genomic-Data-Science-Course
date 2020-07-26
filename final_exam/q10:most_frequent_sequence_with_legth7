""" Which one of the following repeats
of length 7 has a maximum number of occurrences? """

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
        repeats.append(sequence[i:i + 7])
    return repeats

all_seven_repeats = []
for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        all_seven_repeats.append(j)

def most_common(lst):
    return max(set(lst), key=lst.count)

print(most_common(all_seven_repeats))
