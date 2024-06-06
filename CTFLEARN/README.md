# CTFLEARN

# Basic Injection

* Website: https://ctflearn.com/challenge/88

* Solution: It is about **SQL Injection**

    * The *Input* will turn to be 
        ```
        SELECT * FROM webfour.webfour where name = '$input'
        ```
    * We could type the following words to get the all dataset, to make the ' would have the correspondence
        ```
        test' or '1' = '1 
        ```
    

