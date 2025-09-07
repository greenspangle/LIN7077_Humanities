
with open('../project_ACD/testing/test_text.txt', mode ='r', encoding='utf-8') as f:
    for char in f.read():
        # print(char, end = '*')
        pass

# get characters
with open('../project_ACD/testing/test_text.txt', mode='r', encoding='utf-8') as f:
    all_chars = []
    while char:= f.read(1):
        # char = char.lower()
        if char in '012345678abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            # use ord(0) to ord(z) to turn this into simple inequality
            all_chars.append(char)

# count into a dictionary
d={x: 0 for x in '012345678abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}
for char in all_chars:
    d[char] = d[char] +1

print(d)
print(all_chars)


# get characters
with open(r'..\resources\244-0-clean.txt', mode='r', encoding='utf-8') as f:
    all_chars = []
    while char:= f.read(1):
        # char = char.lower()
        if char in '012345678abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            # use ord(0) to ord(z) to turn this into simple inequality
            all_chars.append(char)


# count into a dictionary
scarlet = dict.fromkeys('012345678abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 0)
for char in all_chars:
    scarlet[char] = scarlet[char] +1

print(scarlet)

# need two lists to chart