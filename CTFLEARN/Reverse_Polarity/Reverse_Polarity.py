txt = str(hex(0b01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101))[2:]
FLAG = bytearray.fromhex(txt).decode()
print(FLAG)
