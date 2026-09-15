def prot_dna_rna(seq) -> str:
    codon_groups = {
    "F": "UUU UUC",
    "L": "UUA UUG CUU CUC CUA CUG",
    "S": "UCU UCC UCA UCG AGU AGC",
    "Y": "UAU UAC",
    "Stop": "UAA UAG UGA",
    "C": "UGU UGC",
    "W": "UGG",
    "P": "CCU CCC CCA CCG",
    "H": "CAU CAC",
    "Q": "CAA CAG",
    "R": "CGU CGC CGA CGG AGA AGG",
    "I": "AUU AUC AUA",
    "M": "AUG",
    "T": "ACU ACC ACA ACG",
    "N": "AAU AAC",
    "K": "AAA AAG",
    "V": "GUU GUC GUA GUG",
    "A": "GCU GCC GCA GCG",
    "D": "GAU GAC",
    "E": "GAA GAG",
    "G": "GGU GGC GGA GGG",
    }
    
    codon_table = {
    codon: amino_acid
    for amino_acid, codons in codon_groups.items()
    for codon in codons.split()
    }


    seq = seq.replace("T","U")        
    protein = []
    for i in range(0, len(seq)-2,3):
        amino_acid = codon_table[seq[i:i+3]]
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)
    return ''.join(protein)

if __name__ == "__main__" :
    print("Protein sequence is ",prot_dna_rna(input("RNA or DNA sequence is ")))