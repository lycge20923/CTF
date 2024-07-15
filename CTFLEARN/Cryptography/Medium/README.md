# Cryptography(Medium)

## Substitution_Cipher

* Website: https://ctflearn.com/challenge/238

* Solution: **Right Character to substitute**

    * Use the webstie(https://www.guballa.de/substitution-solver) to find the possible plaintext


* Flag: ```IFONLYMODERNCRYPTOWASLIKETHIS```

## RSA_Noob

* Website: https://ctflearn.com/challenge/120

* Solution: **RSA**

    * It is a simple **RSA**, since its e is 1, which means d is also 1

    * We use to the function ```long_to_bytes``` from ```Cryptodome.Util.number``` to convert a big integer to bytes

* Code: ```python RSA_Noob/RSA_Noob.py```

* Flag: ```abctf{b3tter_up_y0ur_e}```

## 5x5 Crypto

* Website: https://ctflearn.com/challenge/263

* Solution: **grid encryption/decryption**

    * Use ```ABCDE FGHIJ ...``` to get the correspondence

* Flag: ```ctf{thumbs_up}```

## RSA_Beginner

* Website: https://ctflearn.com/challenge/119

* Solution: **RSA**

    * Since the ```e``` is small, we could just use the simple way to decrypt

    * The function ```long_to_bytes(<big integer>)``` from ```Crypto.Util.number``` could convert a big integer to a string

* Code: ```python RSA_Beginner/RSA_Beginner.py```

* Flag: ```abctf{rs4_is_aw3s0m3}```

## 

* Website:

* Solution: 

* Code: 

* Flag: 