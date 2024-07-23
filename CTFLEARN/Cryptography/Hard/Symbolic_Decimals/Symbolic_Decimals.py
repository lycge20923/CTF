cor_dict = dict(zip('!@#$%^&*()', '1234567890'))
encoded = '^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%'
decoded = ''
for ele in encoded:
    if ele not in cor_dict:
        decoded += ele
    else:
        decoded += cor_dict[ele]
decoded = decoded.split(',')
Flag = ''.join([chr(int(ele)) for ele in decoded])
print(Flag)
