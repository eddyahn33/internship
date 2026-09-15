def prot(r_seq) -> str:
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

    protein = []
    Stopped = False
    i = 0
    while Stopped == False:
        amino_acid = codon_table[r_seq[i:i+3]]
        if amino_acid == "Stop":
            Stopped = True
            amino_acid = ""
        protein.append(amino_acid)
        i +=3
        if i > len(r_seq)-3 :
            Stopped = True
        
    return ''.join(protein)

if __name__ == "__main__" :
    print("Protein sequence is ",prot(input("RNA sequence is ")))