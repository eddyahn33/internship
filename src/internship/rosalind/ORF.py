import PROT

def ORF(path):
    with open(path, 'r') as file:
        dna = file.read().splitlines()
        file.close
    dna = "".join(dna[1:])
    rna = dna.replace("T","U")
    revc = ""
    for ch in reversed(rna): 
        if ch == "A" : revc += "U"    
        if ch == "U" : revc += "A"
        if ch == "G" : revc += "C"
        if ch == "C" : revc += "G"

    rnastart = [
        i for i in range(0,len(rna)-2)
        if rna[i:i+3] == "AUG"
    ]
    revcstart = [
        i for i in range(0,len(revc)-2)
        if revc[i:i+3] == "AUG"
    ]
    for i in rnastart:
       PROT.PROT(rna[i:])
    for i in revcstart:
       PROT.PROT(revc[i:])

ORF('/mnt/c/Users/eddya/vscode101/rosalind_solved/rosalind_orf.txt')