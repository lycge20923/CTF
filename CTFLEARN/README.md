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

## Forensics 101 

* Website: https://ctflearn.com/challenge/96

* Solution: **strings instruction**

    * ```strings``` instruction: Would print **printable strings**

    * After conduct ```bash Forensics_101.sh```, it would show the printable strings, and the flag is contained!

* Flag: ```flag{wow!_data_is_cool}```
    

