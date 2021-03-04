# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1:])
print('____________')


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word[3])
print('____________')

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'ауоыиэяюёе'
out_str = []
vowels_qty = 0

for letter in word:
    if letter.lower() in vowels:
        vowels_qty += 1
print(vowels_qty)
print('_____________')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
word_qty = len(sentence.split())
print(word_qty)
print('____________')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
for word in sentence_list:
    print(word[0])
print('____________')

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
word_len_av   = 0.0

for word in sentence_list:
    word_len_av += len(word)

word_len_av /= len(sentence_list)

print(word_len_av)
print('____________')