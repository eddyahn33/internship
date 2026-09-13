def add_odd(a,b):
    result = 0
    if a % 2 == 0:
        i = a+1
        while i <= b:
            result = result + i
            i = i + 2
    else :
        i = a
        while i <= b:
            result = result + i
            i = i + 2
    print("a부터 b까지 홀수의 합은",result, "입니다")

add_odd(int(input("a를 입력하세요")),int(input("b를 입력하세요")))
