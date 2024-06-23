import cv2 
img = cv2.imread("QRCode/qrcode.39907201.png")
import base64

qrcode = cv2.QRCodeDetector()
text, bbox, rectified = qrcode.detectAndDecode(img)
text = base64.b64decode(text).decode()
FLAG = ''
for t in text:
    FLAG += chr(((ord(t) - ord('a') + 13) % 26) + ord('a')) if t.isalpha() else t
print(FLAG)