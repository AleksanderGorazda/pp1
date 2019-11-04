import re

komunikat = "wtorek - 23C, środa - 17C, czwartek - 25C"
cyfry = re.findall('\d{2}',komunikat)
for i in range(len(cyfry)):
    print(cyfry[i])