import hashlib

# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash
# starting with five zeroes is 1048970;
# that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

h = ""
extra = 0
num = 'iwrupvqb'
while not h.startswith("000000"):
    extra += 1
    s = num + str(extra)
    s = s.encode("utf-8")
    h = hashlib.md5(s).hexdigest()

print(extra)
