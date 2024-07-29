encode_text_frag = 'BUGM'
decode_text_frag = 'CTFL'
for en, de in zip(encode_text_frag, decode_text_frag):
    temp_en, temp_de = "{0:b}".format(ord(en)), "{0:b}".format(ord(de))
    print(temp_en, temp_de)

encode_text = 'BUGMdsozc0osx^0r^`vdr1ld|'
flag = ''
for e in encode_text:
    bin_e = ord(e)
    xor_bin_e = bin_e ^ 1
    flag += chr(xor_bin_e)
print(flag)

