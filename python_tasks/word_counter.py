from nltk.tokenize import word_tokenize

text = input('Введите текст в одну строку: ')
words = word_tokenize(text)
search = input('Введите слово для поиска: ').lower()

print(f'Количество вхождений: {words.count(search)}, всего слов: {len(words)}')
