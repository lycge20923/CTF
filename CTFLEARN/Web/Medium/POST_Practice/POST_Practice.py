import os 
import requests

website = 'http://165.227.106.113/post.php'
cmd = 'curl {}'.format(website) 
content = os.popen(cmd).readline().split(' ')
u_key, u_value = content[-6][:-1] ,content[-5]
p_key, p_value = content[-3][:-1], content[-2]
data = {u_key:u_value, p_key:p_value}
r = requests.post(website, data)
FLAG_content = r.content.decode()
FLAG = FLAG_content[FLAG_content.find('flag{'):FLAG_content.find('}')+1]
print(FLAG)