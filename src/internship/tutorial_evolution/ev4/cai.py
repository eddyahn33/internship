import pickle
import math
from pathlib import Path


def gmean(x):
    return math.exp(sum(math.log(value) for value in x) / len(x))

result_file = Path(__file__).with_name("rscu_result.pkl")

with result_file.open('rb') as tf:
    rscu_result = pickle.load(tf)

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

max_rscu = {}
per_codon_cai = {} 

for amino_acid in codon_groups.keys():
    rscu_list = []
    for codon in codon_groups[amino_acid]:
        rscu_list.append(rscu_result[codon])
    max_rscu[amino_acid] = max(rscu_list)

for codon in codon_table.keys():
    per_codon_cai[codon] = rscu_result[codon] / max_rscu[codon_table[codon]]


def cai(codon_list) -> float:
    cai_list = []
    for codon in codon_list:
        cai_list.append(per_codon_cai[codon])
    return gmean(cai_list)


def main():
    seq = input("input CDS sequence ")
    print("CAI value is", cai(seq[i:i+3] for i in range(0,len(seq)-2,3)))

    
if __name__ == "__main__":
    main()