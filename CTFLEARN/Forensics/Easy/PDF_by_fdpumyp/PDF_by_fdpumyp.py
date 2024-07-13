import os 
from base64 import b64decode

os.system('binwalk -e PDF_by_fdpumyp/dontopen.pdf')
os.system('strings PDF_by_fdpumyp/_dontopen.pdf.extracted/B8.zlib > PDF_by_fdpumyp/res.txt')
os.system('rm -r PDF_by_fdpumyp/_dontopen.pdf.extracted/')

with open ('PDF_by_fdpumyp/res.txt', 'r') as f:
    encoded_txt = [ele for ele in f.readlines() if 'external:' in ele][0][9:-1]

os.system('rm PDF_by_fdpumyp/res.txt')
Flag = b64decode(encoded_txt).decode()
print(Flag)
