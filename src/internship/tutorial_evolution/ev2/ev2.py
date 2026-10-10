import random

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

def random_syn_codon(target):
        try:
            syn_list = codon_groups[codon_table[target.upper()]]
            return(random.choice(syn_list))
        except:
            return("Not a codon")

def main():
    print("Randon synonymous codon", random_syn_codon(input("Input Codon ")))

if __name__ == "__main__":
    main()
