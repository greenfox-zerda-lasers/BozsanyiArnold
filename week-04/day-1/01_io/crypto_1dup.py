# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    lines = f.readlines()
    f.close()
    decrypted = ''
    for line in lines:
        for x in range(0,len(line),2):
            decrypted += line[x]
    return decrypted

print(decrypt('texts/duplicated_chars.txt'))
