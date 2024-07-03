import os 
os.system('strings Up_for_a_little_challenge/Begin_Hack.jpg | grep http > Up_for_a_little_challenge/website.txt')
os.system('strings Up_for_a_little_challenge/Begin_Hack.jpg | grep key > Up_for_a_little_challenge/password.txt')


with open('Up_for_a_little_challenge/website.txt', 'r') as f:
    website = f.read().strip().split(' ')[1]
with open('Up_for_a_little_challenge/password.txt', 'r') as f:
    txt = f.read().strip()
    password = txt[txt.find('_key')+6:-1]


print('Go to the website "{}" and download file'.format(website))
os.system('rm Up_for_a_little_challenge/website.txt')
os.system('unzip Up_for_a_little_challenge/Up\ For\ A\ Little\ Challenge.zip -d Up_for_a_little_challenge/')
print('Type the password: {}'.format(password))
os.system('rm Up_for_a_little_challenge/password.txt')
os.system('unzip Up_for_a_little_challenge/Did\ I\ Forget\ Again?/.Processing.cerb4 -d Up_for_a_little_challenge/')



os.system('rm -r Up_for_a_little_challenge/Did\ I\ Forget\ Again?')
os.system('rm -r Up_for_a_little_challenge/__MACOSX')
