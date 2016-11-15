# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    lines = f.readlines()
    f.close
    for x in range(len(lines)):
        lines[x] = lines[x].rstrip()
        lines[x] = lines[x][::-1]
        lines[x] += '\n'
    return "".join(lines)

print(decrypt('texts/reversed_zen_lines.txt'))
