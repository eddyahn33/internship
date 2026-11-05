import random
import argparse
from pathlib import Path
import time

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

codon_change = {
    codon: [c for c in codon_groups[codon_table[codon]] if c != codon]
    for amino_acid, codons in codon_groups.items()
    for codon in codons
}

def n_mutation(codon_list, mutable, mutation_num: int):
    mut_locus = random.sample(mutable,mutation_num)
    result = []

    for i in range(len(codon_list)):
        if i in mut_locus:
            result.append(diff_syn_codon(codon_list[i]))
        else:
            result.append(codon_list[i])      
    return result


def diff_syn_codon(codon):
    return(random.choice(codon_change[codon]))


def positive_int(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("Integer should be over 0")
    return number


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = "Test the mutant creation speed of function"
    )
    parser.add_argument(
        "--m",
        "--mutation-num",
        dest = "mutation_num",
        type = positive_int,
        default = 4,
        help = "number of synonymous mutation created each round (default: 4)",
    )
    return parser.parse_args()


def prot(codon_list):
    protein = []
    for codon in codon_list:
        protein.append(codon_table[codon])
    return protein


def precision(origin, codon_list, mutable, mutation_num):
    correct = 0
    runs = 100000
    for _ in range(runs):
        if prot(n_mutation(codon_list, mutable, mutation_num)) == origin:
            correct += 1
    return f"Correct sequence = {correct}/{runs}"
   
def main():
    args = parse_args()

    with open("test.fasta", 'r') as file:
        file.readline()
        seq = file.read().upper().replace("T","U").replace("\n","")
    codon_list = [seq[i:i+3] for i in range(0, len(seq)-2,3)]
    no_mutation = ["AUG","UGG"]
    mutable = [i for i, codon in enumerate(codon_list) if codon not in no_mutation]
   
    if len(mutable) < args.mutation_num:
        print("Total Codon Number", len(codon_list))
        print("Mutable Codon Number", len(mutable))
        print("Error: not enough mutable codon")
        return None
    print(precision(prot(codon_list), codon_list, mutable, args.mutation_num))
       
if __name__ == "__main__":
    main()

