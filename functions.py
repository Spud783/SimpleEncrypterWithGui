def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()

    



