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
    for codon_tuple in zip(r_seq[::3],r_seq[1::3],r_seq[2::3]):
        amino_acid = codon_table["".join(codon_tuple)]
        if amino_acid == "Stop": break
        protein.append(amino_acid)
    return ''.join(protein)

if __name__ == "__main__" :
    print("Protein sequence is ",prot(input("RNA sequence is ")))