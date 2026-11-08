import re


text = input('текст: ')
words = re.findall(r'[^\W\d_]+', text)
abb = [word for word in words if word.isupper() and len(word) <= 6]

print(abb)