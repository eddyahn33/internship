def ORF(path):
    with open(path, 'r') as file:
        dna = file.readlines()
        dna = dna.pop(0)
        rna = dna.replace("T","U")
        rna = rna.reverse()
        revc = ""
    file.close

    for ch in rna: 
        if ch == "A" : revc += "U"    
        if ch == "U" : revc += "A"
        if ch == "G" : revc += "C"
        if ch == "C" : revc += "G"
    print(revc)
ORF('/mnt/c/Users/eddya/vscode101/rosalind_solved/rosalind_orf.txt')