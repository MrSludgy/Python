# Script should take arguments from execution to simulate
# the full range of polyhedral dice and print the results.
import sys
import re
from random import randint

length=len(sys.argv)
for i in range(1, length):
    diceArg = re.findall('\d+', sys.argv[i])
    diceCount = int(diceArg[0])
    diceRange = int(diceArg[1])
    for j in range(0, diceCount):
      if diceRange>20:
          print('Dice has too many sides. Please try again.')
      elif diceRange%2 == 0:
        print('%d' % randint(1, diceRange))
      else:
        print('%d'% randint(1, diceRange-1))
      if j == diceCount-1:
        print()
