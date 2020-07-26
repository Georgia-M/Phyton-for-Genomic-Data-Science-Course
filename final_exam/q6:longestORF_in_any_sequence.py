'''what is the longest ORF appearing in any sequence and in any forward reading
frame'''

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

def find_orf_1(sequence):
    start_position = 0
    start_indexs = []
    stop_indexs = []
    for i in range(0, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    for i in range(0, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf

def find_orf_2(sequence):
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    for i in range(1, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf

def find_orf_3(sequence):
    start_position = 2
    start_indexs = []
    stop_indexs = []
    for i in range(2, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    for i in range(2, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf



lengths = []
for i in sequences:
    orfs = find_orf_1(i) + find_orf_2(i) + find_orf_3(i)
    for j in orfs:
        lengths.append(len(j))

print(max(lengths))
