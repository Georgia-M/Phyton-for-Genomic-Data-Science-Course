""" What is the starting position of the longest ORF in reading frame 3
in any of the sequences? """

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

# Add the last seq
sequences.append(seq)

sequences = sequences[1:]

# Find orf 3
def find_orf_3(sequence):
    # Find all ATG indexs
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(2, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(2, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                mark = stop_indexs[j]+3
                break
    return orf


position=0
lengths = []
for i in sequences:
    orfs = find_orf_3(i)
    for j in orfs:
        lengths.append(len(j))
#print(max(lengths))

for i in sequences:
    orfs = find_orf_3(i)
    for j in orfs:
        if len(j) == max(lengths):
            #print(len(j))
            position = seq.find(j)

start_position = position + 1

print(start_position)
