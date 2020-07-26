""" Find the most frequently occurring repeat of length 6 in all sequences. How many times does it occur in all? """

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
        repeats.append(sequence[i:i + 6])
    return repeats

all_six_repeats = []
for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        all_six_repeats.append(j)

def most_common(lst):
    return max(set(lst), key=lst.count)

print(all_six_repeats.count(most_common(all_six_repeats)))
