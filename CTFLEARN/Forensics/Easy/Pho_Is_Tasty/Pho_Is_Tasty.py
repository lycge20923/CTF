import os
os.system('hexdump -C Pho_Is_Tasty/Pho.jpg > Pho_Is_Tasty/output.txt')

with open('Pho_Is_Tasty/output.txt', 'r') as f:
    data = f.readlines()[4:9]

print("The flag is in the data:", data)
print("The Flag is: {}".format('CTFlearn{I_Love_Pho!!!}'))