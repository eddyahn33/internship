def main(s,a,b,c,d):
    print(s[a:b+1] + " " + s[c:d+1])


if __name__ == "__main__":
    s = input("string:")
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    main(s,a,b,c,d)
