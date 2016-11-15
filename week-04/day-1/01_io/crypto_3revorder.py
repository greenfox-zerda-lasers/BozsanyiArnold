# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    lines = f.readlines()
    f.close
    decrypted = ''
    for x in range(len(lines)-1):
        lines = lines[::-1]
    return "".join(lines)

print(decrypt('texts/reversed_zen_order.txt'))
