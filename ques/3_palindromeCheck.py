# Examples
# "racecar" → True
# "hello" → False
# "12321" → True
s = "12345" # → False

"""
 noraml method 
s = s.replace(" " ,"").lower()
print(s==s[::-1])

"""

#  Two pointer method
def two_Pointer(s:str) -> bool:
    clear_s = "".join(reversed(s))
    l = 0
    r = len(s) - 1
    while l < r:
        if clear_s[l] != clear_s[r]:
            return False
        l +=1
        r -=1

    return True



print(two_Pointer(s))

