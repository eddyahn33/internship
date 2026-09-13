with open('/mnt/c/Users/eddya/vscode101/rosalind_solved/rosalind_gc.txt', 'r') as file:
    DNA_Strings = file.read().split(">")
    for String in DNA_Strings:
        edit = String.strip("\n")
        print(edit)

file.close