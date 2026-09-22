"""
a. 🌶️ CoCoPUTs database에서 human의 bicodon frequency를 다운로드 받아서 bicodon 버전의 codon adaptation index를 계산한다.
b. CDS서열이 주어지면 CAI를 계산하는 함수를 만든다. 
"""

import argparse
from pathlib import Path
import re


CODON_USAGE_PATTERN = re.compile(
    r"\b([AUCG]{3})\s+\d+(?:\.\d+)?\(\s*(\d+)\)"
)


def parse_codon_usage(input_file: Path) -> dict[str, int]:
    text = input_file.read_text(encoding="utf-8")
    codon_counts = {
        codon: int(count)
        for codon, count in CODON_USAGE_PATTERN.findall(text)
    }
    return codon_counts


def rscu(codon_counts) -> dict[str, int]:
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

    count_dict ={}
    rscu_dict = {}

    for codon, count in codon_counts.items():
        if codon_table[codon] in count_dict.keys():
            count_dict[codon_table[codon]] += count
        else:
            count_dict[codon_table[codon]] = count

    for codon, count in codon_counts.items():
        codon_number = len(codon_groups[codon_table[codon]].replace(" ", ""))/3
        rscu_dict[codon] = codon_number*count/count_dict[codon_table[codon]]

    return rscu_dict

  
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate the RSCU for kazusa codon frequency file"
    )
    parser.add_argument("input_file", type=Path, help="input kazusa codon frequency .txt file")
    return parser.parse_args()


def main() -> dict[str,int]:
    args = parse_args()
    print(rscu(parse_codon_usage(args.input_file)))


if __name__ == "__main__":
    main()
