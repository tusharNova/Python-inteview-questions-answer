

def reverse_string(s : str) -> str:
    #  used rever funtion
    # t = s[::-1]
    # return t

    #  2 used loop
    # t = ""
    # for char in s:
    #     t = char + t
    # return t
    #  build in function

    t = "".join(reversed(s))

    return t


if __name__ == "__main__":
    s = "hello"
    print(reverse_string(s))