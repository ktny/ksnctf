# SYNTがFLAGっぽいことに気づく
# あとは何文字かズラして整合性が取れるか確認するだけ

cipher = input()

from string import ascii_lowercase, ascii_uppercase

for c in cipher:
    if c in ascii_lowercase:
        print(ascii_lowercase[ord(c) % ord('a') - 13], end='')
    elif c in ascii_uppercase:
        print(ascii_uppercase[ord(c) % ord('A') - 13], end='')
    else:
        print(c, end='')
print()
