def main():
    with open('/mnt/c/Users/eddya/vscode101/rosalind_solved/rosalind_ini5.txt', 'r') as f:
        line_number = 1
        for line in f :
            if line_number %2 == 0 :
                print(line, end = "")
            line_number += 1
    f.close

main()