def find_fibonacci(num : int) -> int:
    lis = []
    a , b =0 , 1
    lis.append(a)
    lis.append(b)
    for _ in range(n):
        a , b = b , b+a
        lis.append(b)

    return lis


n = 7

print(find_fibonacci(n))
