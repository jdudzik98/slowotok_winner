

data = {}

letters = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p',
           'q', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']


for single_letter_0 in letters:
    data[str(single_letter_0)] = {}
    for single_letter_1 in letters:
        data[str(single_letter_0)][single_letter_1] = []

with open('slowa.txt') as file:
    words_list = file.read().splitlines()

for word in words_list:
    if len(word) >= 3:
        data[word[0]][word[1]].append(word[2:])


game_letters = [[], [], [], []]

for letter in range(16):
    new_letter = input('Write letter number ' + str(letter + 1))
    if len(new_letter) == 1 and new_letter in letters:
        if letter <= 3:
            game_letters[0].append(new_letter)
        elif letter <= 7:
            game_letters[1].append(new_letter)
        elif letter <= 11:
            game_letters[2].append(new_letter)
        else:
            game_letters[3].append(new_letter)
    else:
        print("That's not a single letter!")


def find_connections(row, column):
    """ Return a list of points, that you can connect given point with"""

    connections = []
    if row != 0:
        connections.append([row-1, column])
        if column != 0:
            connections.append([row-1, column-1])
        if column != 3:
            connections.append([row-1, column+1])
    if row != 3:
        connections.append([row+1, column])
        if column != 0:
            connections.append([row+1, column-1])
        if column != 3:
            connections.append([row+1, column+1])
    if column != 0:
        connections.append([row, column-1])
    if column != 3:
        connections.append([row, column+1])

    return connections


"""

for type in game_letters[0]:
    used_letters = []
    used_letters.append(type)
    next = game_letters[0].index(type)
    if next<=2:
        print(game_letters[0][next+1])
"""
