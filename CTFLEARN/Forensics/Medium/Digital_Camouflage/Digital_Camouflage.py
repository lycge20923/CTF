from base64 import b64decode

psw = 'UEFwZHNqUlRhZQ%3D%3D'
psw = psw.replace('%3D','=')
Flag = b64decode(psw).decode()
print(Flag)
