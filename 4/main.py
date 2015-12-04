import hashlib

def findNumber(zeroes):
    i = 1
    while not hashlib.md5(("iwrupvqb" + str(i)).encode('utf-8')).hexdigest().startswith('0' * 5):
        i += 1
    print(i)

# PART 1
findNumber(5)
# PART 2
findNumber(6)
