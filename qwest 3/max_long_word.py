def max_lond_word():
    file = open('file.txt', 'r', encoding='utf-8')
    read = file.read().split()
    words = []
    words_same_long = []

    for word in read:
        b = word.strip(',.:!')
        words.append(b)

    long_word = max(words, key=len)
    long = len(long_word)

    for word in words:
        if len(word) == len(long_word) and word != long_word:
            words_same_long.append(word)

    print(f'Слово с максимальной длинной в: {long} символов в слове: {long_word}')
    print(f'Cлова с похожей длинной: {words_same_long}')

max_lond_word()