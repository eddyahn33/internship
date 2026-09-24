import math
import csv
from pathlib import Path


def gmean(x):
    return math.exp(sum(math.log(value) for value in x) / len(x))


codon_groups = {
    "F": ["UUU", "UUC"],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "Y": ["UAU", "UAC"],
    "Stop": ["UAA", "UAG", "UGA"],
    "C": ["UGU", "UGC"],
    "W": ["UGG"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "H": ["CAU", "CAC"],
    "Q": ["CAA", "CAG"],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "I": ["AUU", "AUC", "AUA"],
    "M": ["AUG"],
    "T": ["ACU", "ACC", "ACA", "ACG"],
    "N": ["AAU", "AAC"],
    "K": ["AAA", "AAG"],
    "V": ["GUU", "GUC", "GUA", "GUG"],
    "A": ["GCU", "GCC", "GCA", "GCG"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "G": ["GGU", "GGC", "GGA", "GGG"],
    }
    
codon_table = {
    codon: amino_acid
    for amino_acid, codons in codon_groups.items()
    for codon in codons
    }

bicodon_table = {}
for codon1 in codon_table.keys():
    for codon2 in codon_table.keys():
        bicodon_table[codon1 + codon2] = codon_table[codon1] + codon_table[codon2]

bi_amino_list = []
for amino1 in codon_groups.keys():
    for amino2 in codon_groups.keys():
        bi_amino_list.append(amino1 + amino2)

max_bicodon = {}
per_bicodon_cai = {}


with open('human_bicodon_frequency.csv','r') as f:
    csv_dict_reader = csv.DictReader(f)
    for row in csv_dict_reader:
        freq_dict = row
        freq_dict = {
            key.replace("T", "U") : value
            for key, value in freq_dict.items()
        }

for bi_amino in bi_amino_list:
    bi_rscu_list = []
    for bicodon in bicodon_table.keys():
        if bicodon_table[bicodon] == bi_amino:
            bi_rscu_list.append(int(freq_dict[bicodon]))
    max_bicodon[bi_amino] = max(bi_rscu_list)

for bicodon in bicodon_table.keys():
    per_bicodon_cai[bicodon] = int(freq_dict[bicodon]) / max_bicodon[bicodon_table[bicodon]]


def main() -> float:
    input_file = "/home/openclaw/internship/src/internship/tutorial_exercise/ex4/CDS.fasta"
    bicai_list = []
    with open(input_file, 'r') as f:
        rna = f.read().replace("T","U").replace("\n","")

    for i in range(0,len(rna)-5,3):
        bicai_list.append(per_bicodon_cai[rna[i:i+6]])

    print("BiCAI value is", gmean(bicai_list))
    return gmean(bicai_list)


if __name__ == "__main__" :
    main()