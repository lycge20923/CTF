# Cryptography(Easy)

## Character_Encoding

* Website: https://ctflearn.com/challenge/115

* Solution: **Heximal Encoding**

    * Convert the heximal number to the string!

* Code: ```python Character_Encoding/Character_Encoding.py```

    * ```bytearray.fromhex(<hex string>)``` could turn hex number to string. e.g. ```bytearray.fromhex('41') = b'A'```

* Flag: ```ABCTF{45C11_15_U53FUL}```

## Base_2_2_the6

* Website: https://ctflearn.com/challenge/192

* Solution: **Base64 Encoder/Decoder**

    * Base64: Turn ```8-bit```|```8-bit```|```8-bit``` to ```6-bit```|```6-bit```|```6-bit```|```6-bit```, and each 6-bit has a character

* Code: ```python Base_2_2_the6/Base_2_2_the6.py```

* Flag: ```CTF{FlaggyWaggyRaggy}```

## Morse_Code

* Website: https://ctflearn.com/challenge/309

* Solution **Morse Code**

    * Use Morse Code to get the flag information 

* Code: ```python Morse_Code/Morse_Code.py```

* Flag: ```FLAGSAMUELMORSEISCOOLBYTHEWAYILIKECHEES```

## Reverse_Polarity

* Website: https://ctflearn.com/challenge/230

* Solution: **Binary to ASCII**

    * Get the **Hexadecimal** of the number

    * Convert the hexadecimal number to the **byte expression**, using ```bytearray.fromhex(<hex>)```

* Code: ```python Reverse_Polarity/Reverse_Polarity.py```

* Flag: ```CTF{Bit_Flippin}```

## Hextroadinary

* Website: https://ctflearn.com/challenge/158

* Solution: **xor**

    * Xor the two numbers

* Code: ```python Hextroadinary/Hextroadinary.py```

* Flag: ```0xc0ded```

## Vigenere_Cipher

* Website: https://ctflearn.com/challenge/305

* Solution: **Vigenere Cipher**

    * Use the key(in this case, *blorpy*) to decode the ciphertext($C_i - K_i = P_i \mod 26$)

        * $C_i$: Alphabet of ciphertext in position $i$

        * $K_i$: Alphabet of Key in position $i$

        * $P_i$: Alphabet of plantext in position $i$

* Code: ```python Vigenere_Cipher/Vigenere_Cipher.py```

* Flag: ```flag{CiphersAreAwesome}```

## BruXOR

* Website: https://ctflearn.com/challenge/227

* Solution: **Brute Force** & **XOR**

    * Solution 1: Use the website(https://www.dcode.fr/xor-cipher) to brute force search

    * Solution 2: Write the code by ourselves, begin with key = 0 

* Code: ```python BruXOR/BruXOR.py```

* Flag: ```flag{y0u_Have_bruteforce_XOR}```

## HyperStream_Test_2

* Website: https://ctflearn.com/challenge/443

* Solution: **Bacon Cipher**

    * Use the cipher system where letters (I, J) & (U, V) have same ciphertexts

* Code: ```HyperStream_Test_2/HyperStream_Test_2.py```

* Flag: ```ILOUEBACONDONTYOU```