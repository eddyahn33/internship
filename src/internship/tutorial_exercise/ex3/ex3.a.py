#b. 🌶️ 위 프로그램의 parameter, argument 설정을 커멘드라인에서 받는다. click 또는 argparse를 쓸 수 있다.

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
    for i in range(0,len(rna)-2):
        if rna[i:i+3] == "AUG":
            rna_start = i
            break
    protein = []

    for i in range(rna_start, len(rna)-2,3):
        amino_acid = codon_table[rna[i:i+3]]
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)
    return ''.join(protein)

if __name__ == "__main__" :
    input_file = "/home/openclaw/internship/src/internship/tutorial_exercise/ex3/sequence.fasta"
    output_file = "/home/openclaw/internship/src/internship/tutorial_exercise/ex3/protein.fasta"

    with open(input_file, 'r') as f, open(output_file, 'w') as out:
        records = f.read().split(">")
        for record in records:
            if not record:
                continue

            lines = record.splitlines()
            header = lines[0]
            seq = "".join(lines[1:])

            out.write(header)
            out.write("\n")
            out.write(prot_first_orf(seq))
            out.write("\n")
            