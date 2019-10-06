def convert_data():

    """ Function turning words database into dict of dicts of lists for better efficiency"""

    data = {}

    letters = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó',
               'p', 'q', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']

    for single_letter_0 in letters:
        data[str(single_letter_0)] = {}
        for single_letter_1 in letters:
            data[str(single_letter_0)][single_letter_1] = []

    with open('slowa.txt') as file:
        words_list = file.read().splitlines()

    for word in words_list:
        if len(word) >= 3:
           data[word[0]][word[1]].append(word[2:])
    return data

