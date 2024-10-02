# Функции 
text = 'СЪеШЬ еще этих МЯгкиХ француских БулоК'

print(len(text))
print('еще'  in text)
print(text.lower())
print(text.upper())
print(text.replace('еще','ЕЩЕ'))

# Срезы
print(text[0])                              # C
print(text[1])                              # Ъ
print(text[len(text)-1])
print(text[-5])
print(text[:])
print(text[:2])
print(text[len(text)-2:])
print(text[2:9])
print(text[6:-18])
print(text[0:len(text):6])
print(text[::6])
text = text[2:9]+ text[-5] + text[:2]
