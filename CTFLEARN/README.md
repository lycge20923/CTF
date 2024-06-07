# CTFLEARN

## Basic Injection

* Website: https://ctflearn.com/challenge/88

* Solution: **SQL Injection**

    * The *Input* in website https://web.ctflearn.com/web4/ will turn to be 
        ```
        SELECT * FROM webfour.webfour where name = '$input'
        ```
    * We could type the following words to get the all dataset, to make the ' would have the correspondence
        ```
        test' or '1' = '1 
        ```
* Flag: ```CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}```

## Forensics_101 

* Website: https://ctflearn.com/challenge/96

* Solution: **```strings``` Instruction**

    * ```strings <File_name>``` instruction: Would print **printable strings**

* Code: ```bash Forensics_101/Forensics_101.sh```

* Flag: ```flag{wow!_data_is_cool}```
    
## Character_Encoding

* Website: https://ctflearn.com/challenge/115

* Solution: **Heximal Encoding**

    * Convert the heximal number to the string!

* Code: ```python Character_Encoding/Character_Encoding.py```

    * ```bytearray.fromhex(<hex string>)``` could turn hex number to string. e.g. ```bytearray.fromhex('41') = b'A'```

* Flag: ```ABCTF{45C11_15_U53FUL}```

## Taking_LS

* Website: https://ctflearn.com/challenge/103

* Solution: **Check ```.<file_name>``` File**

    * Use ```ls -a``` to check whether there are some ```.<file_name>``` in it!

* Code: ```bash Taking_LS/Taking_LS.sh```

    * ```cat```: print the text in the file

* Flag: ```ABCTF{T3Rm1n4l_is_C00l}```

## Base_2_2_the6

* Website: https://ctflearn.com/challenge/192

* Solution: **Base64 Encoder/Decoder**

    * Base64: Turn 8-bit|8-bit|8-bit to 6-bit|6-bit|6-bit|6-bit, and each 6-bit has a character

* Code: ```python Base_2_2_the6/Base_2_2_the6.py```

* Flag: ```CTF{FlaggyWaggyRaggy}```