from collections import defaultdict

with open('/mnt/c/Users/eddya/vscode101/rosalind_solved/rosalind_ini6.txt', 'r') as f:
    str = f.read()
    dict = defaultdict(int)
    for letter in str.split():
        dict[letter] += 1
    for key, value in dict.items():
        print(key, value)
f.close