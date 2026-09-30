from ev2 import random_syn_codon

def random_syn_cds(cds):
    cds.upper().replace("T","U")
    list = [
        random_syn_codon(cds[i:i+3])
        for i in range(0,len(cds)-2,3)
    ]
    return "".join(list)

def main() -> str:
    with open("/home/openclaw/internship/src/internship/tutorial_evolution/ev2/rna_sequence.txt",'r') as file:
        seq = file.read() 
    return random_syn_cds(seq)

if __name__ == "__main__":
    print(main())