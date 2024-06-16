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