import random
import argparse
from cai import cai

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

def four_mutation(codon_list):
    no_mutation = ["AUG","UGG"]
    mutable = [i for i, codon in enumerate(codon_list) if codon not in no_mutation]

    if len(mutable) < 4:
        print("Total Codon Number", len(codon_list))
        print("Mutable Codon Number", len(mutable))
        print("Error: mutable codon number should be over 4")
        return None
    mut_locus = random.sample(mutable,4)
    result = []

    for i in range(len(codon_list)):
        if i in mut_locus:
            result.append(diff_syn_codon(codon_list[i]))
        else:
            result.append(codon_list[i])       
    return result


def diff_syn_codon(codon):
    change = [c for c in codon_groups[codon_table[codon]] if c != codon]
    return(random.choice(change))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = "Create 4 synonymous mutations each round for given CDS and # of rounds"
    )
    parser.add_argument("input_file", help = "RNA/DNA CDS txt file name")
    parser.add_argument("mut_round", type = int, help = "iteration # of mutation")
    
    return parser.parse_args()


def evolution(codon_list, rounds):   
    current = codon_list

    if four_mutation(current) is None:
        return None #mutable 4개 없는 경우 예외처리
    
    for round in range(rounds):
        current = four_mutation(current)
        print(f"{round+1} round CAI:", cai(current))
    return(current)


def main():
    args = parse_args()
    with open(args.input_file, 'r') as file:
        file.readline()
        seq = file.read().upper().replace("T","U").replace("\n","")
    codon_list = [seq[i:i+3] for i in range(0, len(seq)-2,3)]
    print("Original CAI:" , cai(codon_list))
    final_seq = evolution(codon_list, args.mut_round)
    return(final_seq)


if __name__ == "__main__":
    main()