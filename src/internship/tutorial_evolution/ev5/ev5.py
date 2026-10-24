import random
import argparse
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

rscu_result = {
    'UUU': 0.9282685397565936, 'UCU': 1.1255150408606662, 'UAU': 0.886676218533842, 'UGU': 0.9123146610073367, 'UUC': 1.0717314602434065, 'UCC': 1.3077571899552556, 'UAC': 1.1133237814661578, 'UGC': 1.0876853389926633, 'UUA': 0.4594058735061771, 'UCA': 0.903102888109628, 'UAA': 0.8910573541447014, 'UGA': 1.3987289041590787, 'UUG': 0.7743471222412242, 'UCG': 0.32638628231303446, 'UAG': 0.7102137416962199, 'UGG': 1.0, 'CUU': 0.7902954723890413, 'CCU': 1.1469253186281112, 'CAU': 0.8370304256867382, 'CGU': 0.48064516828920617, 'CUC': 1.173460955486913, 'CCC': 1.2938815925154203, 'CAC': 1.1629695743132618, 'CGC': 1.1026597787386934, 'CUA': 0.4282810338808536, 'CCA': 1.1064101105504769, 'CAA': 0.5300335184203467, 'CGA': 0.652874899924713, 'CUG': 2.374209542495791, 'CCG': 0.4527829783059915, 'CAG': 1.4699664815796532, 'CGG': 1.2093260404032953, 'AUU': 1.0832165790361832, 'ACU': 0.9870753760664156, 'AAU': 0.9407339814936057, 'AGU': 0.8976109380580557, 'AUC': 1.409598868500986, 'ACC': 1.4209261629756786, 'AAC': 1.0592660185063942, 'AGC': 1.43962766070336, 'AUA': 0.507184552462831, 'ACA': 1.1367509193556742, 'AAA': 0.8680987022041431, 'AGA': 1.287946487655754, 'AUG': 1.0, 'ACG': 0.45524754160223163, 'AAG': 1.131901297795857, 'AGG': 1.266547624988338, 'GUU': 0.7270804472139485, 'GCU': 1.0636864568565494, 'GAU': 0.9290848383860854, 'GGU': 0.6523460526531788, 'GUC': 0.9532255182454069, 'GCC': 1.5991244853745878, 'GAC': 1.0709151616139145, 'GGC': 1.3484374323777801, 'GUA': 0.46630964213402726, 'GCA': 0.9124850526865104, 'GAA': 0.8449053256072323, 'GGA': 0.9996866059876165, 'GUG': 1.8533843924066173, 'GCG': 0.42470400508235245, 'GAG': 1.1550946743927677, 'GGG': 0.9995299089814247
}

max_rscu = {}
for amino_acid in codon_groups.keys():
    rscu_list = []
    for codon in codon_groups[amino_acid]:
        rscu_list.append(rscu_result[codon])
    max_rscu[amino_acid] = max(rscu_list)

per_codon_cai = {} 
for codon in codon_table.keys():
    per_codon_cai[codon] = rscu_result[codon] / max_rscu[codon_table[codon]]

def gmean(x):
    return math.exp(sum(math.log(value) for value in x) / len(x))


def cai(codon_list) -> float:
    cai_list = []
    for codon in codon_list:
        cai_list.append(per_codon_cai[codon])
    return gmean(cai_list)


def n_mutation(codon_list, mutation_num):
    no_mutation = ["AUG","UGG"]
    mutable = [i for i, codon in enumerate(codon_list) if codon not in no_mutation]

    if len(mutable) < mutation_num:
        print("Total Codon Number", len(codon_list))
        print("Mutable Codon Number", len(mutable))
        print("Error: not enough mutable codon")
        return None
    mut_locus = random.sample(mutable,mutation_num)
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


def positive_int(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("Integer should be over 0")
    return number


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = "Create # synonymous mutations each round for given CDS and # of rounds"
    )
    parser.add_argument(
        "input_file",
        type = Path,
        help = "RNA/DNA CDS file path",
    )
    parser.add_argument(
        "-m",
        "--mutation-num",
        type = positive_int,
        default = 4,
        help = "number of synonymous mutation created each round (default: 4)",
    )
    parser.add_argument(
        "-c",
        "--child-num",
        type = positive_int,
        default = 10,
        help = "number of mutant children created each round (default: 10)",
    )
    parser.add_argument(
        "-r",
        "--mut-round",
        type = positive_int,
        default = 1000,
        help = "number of mutation round (default: 1000)",
    )
    parser.add_argument(
        "-n",
        "--runs",
        type = positive_int,
        default = 1,
        help = "number of individual runs (default: 1)",
    )
    return parser.parse_args()


def evolution(codon_list, mutNum, children, rounds):   
    current = codon_list.copy()

    mutable_count = sum(codon not in ("AUG", "UGG") for codon in current)
    if mutable_count < mutNum:
        print("Total Codon Number", len(current))
        print("Mutable Codon Number", mutable_count)
        return None

    cai_values = [cai(current)]
    
    for round in range(rounds):
        fittest = n_mutation(current,mutNum)

        for i in range(children - 1):
            mutant = n_mutation(current, mutNum)
            if cai(mutant) > cai(fittest):
                fittest = mutant
        cai_values.append(cai(fittest))
        current = fittest
    return cai_values



def main():
    args = parse_args()

    with open(args.input_file, 'r') as file:
        file.readline()
        seq = file.read().upper().replace("T","U").replace("\n","")
    codon_list = [seq[i:i+3] for i in range(0, len(seq)-2,3)]

    for run in range(args.runs):
        cai_list = evolution(codon_list, args.mutation_num, args.child_num, args.mut_round)

        max_index = max(range(len(cai_list)), key = cai_list.__getitem__)
        max_cai = cai_list[max_index]

        if cai_list is None:
            raise SystemExit(f"The FASTA sequence must contain {args.mutation_num} mutable codons.")
 
        plt.plot(
            range(len(cai_list)),
            cai_list,
            alpha=0.6,
            linewidth=0.8,
            label=f"Run {run + 1}" if args.runs <= 10 else None,
        )
        plt.scatter(max_index, max_cai, color="red", s=24, zorder=3)

        if args.runs <= 8:
            plt.annotate(
                f"{max_cai:.3f}",
                (max_index, max_cai),
                xytext=(5, 5),
                textcoords="offset points",
                fontsize=8,
            )

    plt.xlabel("Cycle")
    plt.ylabel("CAI")
    input_path = Path(args.input_file)
    plt.title(
    f"CAI change of {input_path.stem}\n"
    f"mutation_num={args.mutation_num}, "
    f"child_num={args.child_num}, "
    f"mut_round={args.mut_round}, "
    f"runs={args.runs}"
    )
    plt.grid(True)
    if args.runs <= 8:
        plt.legend(loc="lower right", fontsize=8)
    output_path = input_path.with_name(
    f"{input_path.stem}_CAI"
    f"_mutations-{args.mutation_num}"
    f"_children-{args.child_num}"
    f"_rounds-{args.mut_round}"
    f"_runs-{args.runs}.png"
    )
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Saved combined plot to {output_path}")

if __name__ == "__main__":
    main()