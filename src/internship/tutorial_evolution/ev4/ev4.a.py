import random
import argparse
import pickle
import math
from pathlib import Path
import matplotlib.pyplot as plt

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



def gmean(x):
    return math.exp(sum(math.log(value) for value in x) / len(x))

result_file = Path(__file__).with_name("rscu_result.pkl")

with result_file.open('rb') as tf:
    rscu_result = pickle.load(tf)

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
    parser.add_argument(
        "--runs",
        type = int,
        default = 1,
        help = "number of independent runs to plot together (default: 1)",
    )
    
    return parser.parse_args()


def evolution(codon_list, rounds):   
    current = codon_list.copy()

    mutable_count = sum(codon not in ("AUG", "UGG") for codon in current)
    if mutable_count < 4:
        print("Total Codon Number", len(current))
        print("Mutable Codon Number", mutable_count)
        return None

    cai_values = [cai(current)]
    
    for round in range(rounds):
        fittest = four_mutation(current)

        for i in range(9):
            mutant = four_mutation(current)
            if cai(mutant) > cai(fittest):
                fittest = mutant
        cai_values.append(cai(fittest))
        current = fittest
    return cai_values



def main():
    args = parse_args()
    if args.runs < 1:
        raise SystemExit("--runs must be at least 1")

    with open(args.input_file, 'r') as file:
        file.readline()
        seq = file.read().upper().replace("T","U").replace("\n","")
    codon_list = [seq[i:i+3] for i in range(0, len(seq)-2,3)]

    for run in range(args.runs):
        cai_list = evolution(codon_list, args.mut_round)
        if cai_list is None:
            raise SystemExit("The FASTA sequence must contain at least 4 mutable codons.")
        plt.plot(
            range(len(cai_list)),
            cai_list,
            alpha=0.6,
            linewidth=0.8,
            label=f"Run {run + 1}" if args.runs <= 10 else None,
        )

    plt.xlabel("Cycle")
    plt.ylabel("CAI")
    input_path = Path(args.input_file)
    plt.title(f"CAI change of {input_path.stem} ({args.runs} runs)")
    plt.grid(True)
    if args.runs <= 10:
        plt.legend(loc="lower right", fontsize=8)
    output_path = input_path.with_name(f"{input_path.stem}_{args.runs}R_result.png")
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Saved combined plot to {output_path}")


if __name__ == "__main__":
    main()