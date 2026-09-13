def main() -> None:
    A = 0
    C = 0
    G = 0
    T = 0
    for ch in input("DNA sequence here"):
        if ch == "A":
            A += 1
        elif ch == "C":
            C += 1
        elif ch == "G":
            G += 1
        else:
            T += 1
    print (A, C, G, T)
if __name__ == "__main__":
    main()