

def func(text, s=''):
    if text == '':
        return s == ''

    if text[0] == '(':
        return func(text[1:], s + ')')
    if text[0] == '[':
        return func(text[1:], s + ']')
    if text[0] == '{':
        return func(text[1:], s + '}')
    if text[0] in ')]}':
        if s == '' or text[0] != s[-1]:
            return False
        return func(text[1:], s[:-1])

    return func(text[1:], s)

text = input('текст: ')
print(func(text))