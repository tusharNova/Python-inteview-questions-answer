


s = [12 ,3 , 14 ,7 ,5 , 9]

n = len(s)

for i in range(n - 1):
    for j in range(n-i-1):
        if s[j] > s[j+1]:
            s[j] ,s[j+1] = s[j+1] , s[j]


print(s)
