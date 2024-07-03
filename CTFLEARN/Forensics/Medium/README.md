# Forensics(Medium)

## 07601

* Website: https://ctflearn.com/challenge/97

* Solution: ```binwalk``` & ```strings```

    * Use ```binwalk -e <file>``` to anlyze the file. It would thoroughly extract the files hidden in the ```<file>```

    * Then, use ```strings``` to extract information in it 

* Code: ```bash 07601/07601.sh```

* Flag: ```ABCTF{Du$t1nS_D0jo}```



## Milk_Best_Friend

* Website: https://ctflearn.com/challenge/195

* Solution: **binwalk**, **unrar** and **strings**

    * steps

        1. ```binwalk <A.img>``` 

        3. ```strings <B.img>```

* Code: ```bash Milk_Best_Friend/Milk_Best_Friend.sh```

* Flag: ```flag{eat_more_oreos}```

## A_CAPture_of_Flag

* Website: https://ctflearn.com/challenge/356

* Solution: **Wireshark** and message

    * Use **Wireshark** to open the file 

    * We could then find the message is encoded, it is obviously **b64-encoded**: 

        ![image.png](A_CAPture_of_Flag/image.png)

* Flag: ```flag{AFlagInPCAP}```

## Up_For_A_Little_Challenge

* Website: https://ctflearn.com/challenge/142

* Solution: **Observation** & ```.perb```

    * 從```strings <File>```中搜尋自己要的資料，包含另一個檔案網址和密碼

    * 然後透過適當解壓縮（當中包含```.perb```也要）來完成

* Code: ```python Up_for_a_little_challenge/Up For A Little Challenge.zip```

* Flag: 

## 

* Website: 

* Solution: 

    * 

* Code: 

* Flag: 

