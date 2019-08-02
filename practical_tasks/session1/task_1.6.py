def get_longest_world(phrase: str) -> str:
    word_def, arr = '', []

    arr = phrase.split(' ')
    for word in arr:
        if len(word) > len(word_def):
            word_def = word

    return word_def


print(get_longest_world('hi said sasha and waved his hand, stop it immediately yield petya'))
