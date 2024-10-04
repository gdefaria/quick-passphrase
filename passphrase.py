import os
import sys
from math import log2
from random import SystemRandom

# Secure randomness
random = SystemRandom()

# Locating file also when it's an executable
base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))

# Load EFF extended wordlist for diceware securely
wordlist = open(os.path.join(base_path, './wordlist.txt'), 'r').read().split('\n')
entropyPerWord = log2(len(wordlist))

# Ensure length argument is a valid integer
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    length = int(sys.argv[1])
else:
    print('Invalid length')
    sys.exit(1)

passphrase = []

for _ in range(length):
    index = random.randint(0, len(wordlist) - 1)
    word = wordlist[index].split('\t')[1]
    passphrase.append(word)

# Display passphrase with temporary visibility and clear sensitive variables
print(f'{" ".join(passphrase)} - entropy: {round(entropyPerWord * length, 2)} bits')

# Clear sensitive data
del passphrase, word, wordlist, entropyPerWord