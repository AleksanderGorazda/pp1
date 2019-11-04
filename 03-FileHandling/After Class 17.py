import re

komunikat = "To be, or not to be, that is the question"
samogloski = re.findall('a|e|y|u|i|o',komunikat)
print(len(samogloski))