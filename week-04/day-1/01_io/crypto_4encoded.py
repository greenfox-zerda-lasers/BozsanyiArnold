# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
        f = open(file_name)
        lines = f.readlines()
        f.close
        decrypted = ''
        for line in lines:
            for i in line:
                if i != ' ' and i != '\n':
                    decrypted += chr(ord(i)-1)
                else:
                    decrypted += i
        return decrypted


print(decrypt('texts/encoded_zen_lines.txt'))
