# Forensics(Easy)

## Forensics_101 

* Website: https://ctflearn.com/challenge/96

* Solution: **```strings``` Instruction**

    * ```strings <File_name>``` instruction: Would print **printable strings**

* Code: ```bash Forensics_101/Forensics_101.sh```

* Flag: ```flag{wow!_data_is_cool}```

## Taking_LS

* Website: https://ctflearn.com/challenge/103

* Solution: **Check ```.<file_name>``` File**

    * Use ```ls -a``` to check whether there are some ```.<file_name>``` in it!

* Code: ```bash Taking_LS/Taking_LS.sh```

    * ```cat```: print the text in the file

* Flag: ```ABCTF{T3Rm1n4l_is_C00l}```

## WOW_So_Meta

* Website: https://ctflearn.com/challenge/348

* Solution: **```strings``` Instruction**

    * ```strings <file>```: To check information of the file

    * ```grep <strings>```: Grep something in the output text of the terminal

* Code: ```bash WOW_So_Meta/WOW_So_Meta.sh```

* Flag: ```flag{EEe_x_I_FFf}```

## Binwalk

* Website: https://ctflearn.com/challenge/108

* Solution: **Binwalk**

    * A tool for analyzing **binary files**
    
    * Commonly used: Penetration testing, analyze the contents within binary files, including data embedded in firmware, image files, compressed files, and more.

* Code: ```bash CTFLEARN/Binwalk/Binwalk.sh```

* Flag: ```ABCTF{b1nw4lk_is_us3ful}```

## Exif

* Website: https://ctflearn.com/challenge/303

* Solution: **```strings``` Instruction**

    * Use ```strings <file>``` and add ```grep flag``` to catch the text about flag

* Code: ```bash Exif/Exif.sh```

* Flag: ```flag{3l1t3_3x1f_4uth0r1ty_dud3br0}```

## Rubber_Duck

* Website: https://ctflearn.com/challenge/933

* Solution: **```strings``` Instruction**

    * Use ```strings <file>``` and add ```grep {``` to catch the text about flag

* Code: ```bash Rubber_Duck/Rubber_Duck.sh```

* Flag: ```CTFlearn{ILoveJakarta}```

## Git_Is_Good

* Website: https://ctflearn.com/challenge/104

* Solution: ```git show```

    * ```git show ___```: 用來查看某次的提交細節。若為```git show head```，則為秀最後一次的提交

* Code

    ```
    cd Git_Is_Good/gitIsGood
    git show HEAD
    ```

* Flag: ```flag{protect_your_git}```

## Im_a_dump

* Website: https://ctflearn.com/challenge/883

* Solution: ```strings```

    * After conducting ```strings <file>```, there would be the  information similar to flag, we could then delete ```H, E, U```

* Code: ```bash Im_a_dump/Im_a_dump.sh```

* Flag: ```CTFlearn{fl4ggyfl4g}```

## Snowboard 

* Website: https://ctflearn.com/challenge/934

* Solution: ```strings``` & ```base64```

    * There would be base64-encoded flag in the first lines of ```strings <file>```

* Code: ```python Snowboard/Snowboard.py```

* Flag: ```CTFlearn{SkiBanff}```

## Pho_Is_Tasty

* Website: https://ctflearn.com/challenge/971

* Solution: **```hexdump```**

    * ```hexdump -C```: Represent a file with the format of the correspondence(**Heximal**, **ASCII**)

* Code: ```python Pho_Is_Tasty/Pho_Is_Tasty.py```

* Flag: ```CTFlearn{I_Love_Pho!!!}```

## PDF_by_fdpumyp

* Website: https://ctflearn.com/challenge/957

* Solution: ```binwalks```, ```strings```

    * ```binwalks``` the file and extract the files, and ```strings``` the extracted files to find the specific text

* Code: ```python PDF_by_fdpumyp/PDF_by_fdpumyp.py```

* Flag: ```CTFlearn{)_1l0w3y0Um00my123}```

## Minions

* Website: https://ctflearn.com/challenge/955

* Solution: ```Binwalk``` & ```strings``` & ```b64decode```

    * Keep try ```Binwalk``` and ```strings```, and decode the text after seeing ```CTF{``` 

* Code: ```python Minions/Minions.py```

* Flag: ```CTF{M1NI0NS_ARE_C00L```

## GandalfTheWise

* Website: https://ctflearn.com/challenge/936

* Solution: ```b64decode(<b64 encrypted text>)``` & ```long_to_bytes(<integer>)``` from ```Crypto.Util.number```

    * If we need to convert a string, which is likely a b64-represent text, into a integer(10-base/16-base) => ```int(b64decode(<b64 encrypted text>).hex(), 16)``` to turn it to be hex.

    * Instead, if we need to convert a hex number to a string => ```long_to_byes(<heximal text>)```

* Code: ```python GandalfTheWise/GandalfTheWise.py```

* Flag: ```CTFlearn{Gandalf.BilboBaggins}```

## Blank_Page

* Website: https://ctflearn.com/challenge/959

* Solution: **Observation**

    * We could use ```repr()``` to find the content even if there seen to be empty in the file

* Code: ```python Blank_Page/Blank_Page.py```

* Flag: ```CTFlearn{If_y0u_r3/\d_thi5_you_pa553d}```

## 

* Website:

* Solution: 

* Code:

* Flag: 