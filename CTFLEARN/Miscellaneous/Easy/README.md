# Miscellaneous(Easy)

## Where_Can_My_Robot_Go

* Website: https://ctflearn.com/challenge/107

* Solution: ```robots.txt```

    * One text file placing under ```root```

    * Purpose: Tell the **Web Crawlers/Web Browser** which page could be crawled or not

    * Structure:
        
        * ```User-agent```: The rule would be applied to which web crawlers, often is ```*```
        
        * ```Disallow```: Disallow the path that web crawlers crawl

        * Example1: When we don't want ```/private``` to be accessed
            ```
            User-agent: *
            Disallow: /private/
            ```
        * Example2: When we allow all pages to be accessed
            ```
            User-agent: *
            Disallow: 
            ```
    
    * ```curl <website>```: Visit the content in ```<website>``` 

* Code: ```bash Where_Can_My_Robot_Go/Where_Can_My_Robot_Go.sh```

* Flag: ```CTFlearn{r0b0ts_4r3_th3_futur3}```

## Wikipedia

* Website: https://ctflearn.com/challenge/168

* Solution: **Edit History(Diff)**

    * Search for ```128.125.52.138``` in English Wikipedia => Check ```Diff``` => See the flag

* Flag: ```cNi76bV2IVERlh97hP```

## QRCode

* Website: https://ctflearn.com/challenge/228

* Solution: **Base 64 decod** & **ROT 13**

    * Just decode by base-64 decoding and ROT 13

* Code: ```python QRCode/QRCode.py```

Flag: ```n0_body_f0rget_qr_code```