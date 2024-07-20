# Forensics(Hard)

## Corrupted_File

* Website: https://ctflearn.com/challenge/138

* Solution: ```Hex Fiend``` & ```Edit File```

    * We first examine the ```unopenable.gif```, and we could find that the ```git``` file start with ```39 61```

        ![Corrupted_File_1](Corrupted_File/1.png)
    
    * However, the first hex number of the ```gif``` file starts with ```47 49 46 38 39 61```. Therefore, we need to edit the file 

    * By using ```HexFiend```, we could fix the gif file

        ![Corrupted_File_2](Corrupted_File/2.png)

    * Then, there are some hints in the frames of the gif file. We could **Split the gif** to get the detailed information:

        ```the flag is ZmxhZ3tnMWZfb3JfajFmf@== DECODE IT```

        ![Corrupted_File_3](Corrupted_File/3.png)
    
    * We could then decode it and get the flag!

* Flag: ```flag{g1f_or_j1f}```

## 

* Website: 

* Solution: 

* Code: ``````

* Flag: ``````
