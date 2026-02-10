s = [12 ,3 , 14 ,7 ,5 , 9]

fisth , seconfh = -1 , -1

for i in s:
    if i > fisth:
        seconfh = fisth
        fisth = i
    elif i >seconfh and i!=fisth:
        seconfh = i


print(fisth)
print(seconfh)
