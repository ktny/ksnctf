# 最後の行に下記のようにあるので辞書をダウンロード
# SHA512IsStrong$DictionaryIsHere.http//ksnctf.sweetduet.info/q/14/dicti0nary_8Th64ikELWEsZFrf.txt
# john the ripperで辞書攻撃
# john --wordlist=dictionary users
# john --show users
# 8文字目をつなげる
ans = []
for i in range(21):
    s = input()
    ans.append(s[7])
print(*ans, sep='')
