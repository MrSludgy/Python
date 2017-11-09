import random
import string
import sys
length=int(sys.argv[1])
x = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
print(x)
