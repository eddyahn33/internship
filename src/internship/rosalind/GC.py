def GC_max(path):
    with open(path,'r') as file:
        f = file.read().replace("\n","")
    file.close

    DNA_list = f.split(">")
    DNA_list.pop(0)

    GC_percent = {}
    for DNA in DNA_list:
        name = DNA[0:13]
        seq = DNA[13:]  
        GC_percent[name] = (seq.count("G")+ seq.count("C"))/len(seq)*100
    name, percentage = max(GC_percent.items(),key=lambda item : item[1])
    print(name)
    print(percentage)
GC_max('/mnt/c/Users/eddya/vscode101/rosalind_solved/rosalind_gc.txt')