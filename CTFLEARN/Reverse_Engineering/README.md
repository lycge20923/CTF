# Reverse_Engineering

## Reykjavik

* Website: https://ctflearn.com/challenge/990

* Solution: **Reverse Engineering**

    * What is **Reverse Engineering**: Analyze software system to identify components and its work, step including 

    * The ```GDB``` is useful for **Reverse Engineering**

    * Steps(Execute in Linux OS)

        1. First, we execute the file using ```ReyKjavik```, then we follow the instruction to execute using ```Reykjavik CTFlearn{flag}```, we get the false flag

            ![ReyKjavik](ReyKjavik/1.png)
        
        2. We then start use **```gdb```**

            ![ReyKjavik](ReyKjavik/2.png)

            * ```-q```: quiet mode, only show necessary information
        
        3. Then, we execute by ```disassemble main```, this is to turn the machine language into readable codes

            ![ReyKjavik](ReyKjavik/3.png)

        4. We could see that in the 200th line, there is about ```call   0x1080 <strcmp@plt>```. We can set a breakpoint(let the code keep executing until touch the line) there and execute the program

            ![ReyKjavik](ReyKjavik/4.png)

            ![ReyKjavik](ReyKjavik/5.png)
        
        5. Run the code: ```run 'CTFlearn{flag}'```, and we could find that the first parameter(which is for comparing the string) for ```strcmp``` is in ```$rdi```

            ![ReyKjavik](ReyKjavik/6.png)

        6. We could then use ```x/s $rdi``` to see the ```$rdi```, which storing the correct flag.

            ![ReyKjavik](ReyKjavik/7.png)

* Flag: ```CTFlearn{Eye_L0ve_Iceland_}```

## 

* Website: 

* Solution:

* Code:

* Flag: 