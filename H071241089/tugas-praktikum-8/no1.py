import re

s = str(input("Masukkan string : "))
pattern = r"[A-Za-z(2|4|6|8)]{40}[(1|3|5|7|9| )]{5}"

result = re.match(pattern, s)

if len(s) > 45 or len(s) < 45:
    print(False)
elif result:
    print(True)
else:
    print(False)

