#Generates an alphanumeric string of a given length
import random
import string
import sys

length=int(sys.argv[1])

def main():
  x = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
  print(x)

if sys.argv[0] == 'alphanumeric.py':
  main()
