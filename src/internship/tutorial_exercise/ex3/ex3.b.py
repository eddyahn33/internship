import argparse
from pathlib import Path

def prot_first_orf(seq) -> str:
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

    rna = seq.replace("T","U")        
    rna = seq.replace("T","U")        
    rna_start = rna.find("AUG")
    protein = []

    if rna_start == -1 :
        return "None"

    for i in range(rna_start, len(rna)-2,3):
        amino_acid = codon_table[rna[i:i+3]]
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)
    return ''.join(protein)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate the first AUG-started ORF in each FASTA sequence."
    )
    parser.add_argument("input_file", type=Path, help="input RNA/DNA FASTA file")
    parser.add_argument("output_file", type=Path, help="output protein FASTA file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    with args.input_file.open("r") as f, args.output_file.open("w") as out:
        records = f.read().split(">")
        for record in records:
            if not record:
                continue

            lines = record.splitlines()
            header = lines[0]
            seq = "".join(lines[1:])

            out.write(">" + header)
            out.write("\n")
            out.write(prot_first_orf(seq))
            out.write("\n")


if __name__ == "__main__":
    main()
            
