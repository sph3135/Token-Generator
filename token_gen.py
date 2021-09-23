import random
l = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
s = "?/*+-=,@#$%&_"
tot = l + u + num + s
len = 16
token = "".join(random.sample(tot, len))
print(token)