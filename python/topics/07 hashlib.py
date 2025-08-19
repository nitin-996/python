import hashlib

pwd = "this is DB password"

# password is string so i have to convert it inot binary string and then hash it

bsecret = pwd.encode()

pwdhash = hashlib.md5()

pwdhash.update(bsecret)
print(pwdhash.digest())