indexes = []
letters = []

word = input("Введите Ваше слово: ")
for index, letter in enumerate(word):
    indexes.append(index)
    letters.append(letter)
i = len(word)
if i % 2 == 0:
    middle_index1 = i // 2 - 1
    middle_index2 = i // 2
    middle_letter1 = letters[middle_index1]
    middle_letter2 = letters[middle_index2]
    print('Word ' + word)
    print("Результат: ", middle_letter1+middle_letter2)
else:
    middle_index = i // 2
    middle_letter = letters[middle_index]
    print('Word ' + word)
    print("Результат: ", middle_letter)
