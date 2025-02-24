def hashing(string):
    p = 31
    m = 1000007
    val = 0
    for char in string:
        val = (val * p + ord(char)) % m
    return val