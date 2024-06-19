lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa',
          'K': 'abaab', 'L': 'ababa', 'M': 'ababb', 'N': 'abbaa', 'O': 'abbab',
          'P': 'abbba', 'Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba',
          'U': 'baabb', 'W': 'babaa', 'X': 'babab', 'Y': 'babba', 'Z': 'babbb'}
decipher = dict(zip(lookup.values(), lookup.keys()))
ciphertext = 'ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB'
FLAG = ''
for i in range(0, len(ciphertext), 5):
    FLAG += decipher[ciphertext[i:i+5].lower()]
print(FLAG)