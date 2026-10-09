import random
from pathlib import Path
import argparse

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

def mutation(codon_list,mut_num):
    no_mutation = ["AUG","UGG"]
    mutable = [i for i, codon in enumerate(codon_list) if codon not in no_mutation]
    print("Total Codon Number", len(codon_list))
    print("Mutable Codon Number", len(mutable))
    if len(mutable) == 0:
        print("No mutable codon")
        return None
    elif mut_num > len(mutable):
        print("Error: Input number exceeds mutable codon number")
        return None
    mut_locus = random.sample(mutable,mut_num)
    result = []

    for i in range(len(codon_list)):
        if i in mut_locus:
            result.append(diff_syn_codon(codon_list[i]))
        else:
            result.append(codon_list[i])       
    return "".join(result)

def diff_syn_codon(codon):
    change = codon_groups[codon_table[codon]].copy()
    change.remove(codon)
    return(random.choice(change))

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create synonymous mutations for given CDS and # of mutation"
    )
    parser.add_argument("-i", "--input-file", required = True, help = "RNA/DNA CDS txt file name")
    parser.add_argument("-m", "--num-mutations", type = int, required = True, help = "number of mutation")

    return parser.parse_args()

def main():
    args = parse_args()
    with open(args.input_file, 'r') as file:
        seq = file.read().upper().replace("T","U")
        codon_list = [seq[i:i+3] for i in range(0, len(seq)-2,3)]
    result = mutation(codon_list,args.num_mutations)
    if result == None:
        return
    else:
        with open('out_' + args.input_file, 'w') as out:
            out.write(result)
            print("Mutation Complete")
    
if __name__ == "__main__":
    main()