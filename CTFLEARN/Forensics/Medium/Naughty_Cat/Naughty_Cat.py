import os 
from base64 import b64decode

os.system('binwalk -e Naughty_Cat/cut3_c4t.png')
os.system('unrar e Naughty_Cat/_cut3_c4t.png.extracted/28E4B.rar Naughty_Cat/')
os.system('rm -r Naughty_Cat/_cut3_c4t.png.extracted/')

'''
Next step: 
1. modify the rar file, using Hex Field
2. Analyze the audio, using spectrum analyzer(https://academo.org/demos/spectrum-analyzer/) to find the password
'''
password = 'sp3ctrum_1s_y0ur_fr13nd'
os.system('unrar e -p{} Naughty_Cat/y0u_4r3_cl0s3_fixed.rar Naughty_Cat/'.format(password))

'''
We then check the final txt and decode
'''

encoded_txt = 'ZjByM241MWNzX21hNXQzcg=='
Flag = b64decode(encoded_txt).decode()
print(Flag)

os.system('rm Naughty_Cat/y0u_4r3_cl0s3.rar | rm Naughty_Cat/purrr_2.mp3 | rm Naughty_Cat/f1n4lly.txt')
