import random

from pip._vendor.distlib.compat import raw_input

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w",
            "x", "y", "z"]


def removeLetter(alphabet):
    global symbol
    can_remove = [("v", "w"), ("k", "c"), ("j", "i"), ("w", "v"), ("c", "k")]
    symbol = can_remove[random.randint(0, 4)]  # remember this symbol, żeby zamienić to w szyfrowanym słowie
    new_list = [x for x in alphabet if x is not symbol[0]]
    return new_list


def modifyAlphabet(alphabet, word):
    return removeDuplicates(removeLetter(list(word) + alphabet))


# macierz z alfabetem
def removeDuplicates(alphabet):
    unique = []
    for elem in alphabet:
        if elem not in unique:
            unique.append(elem)
    return unique


def substituteLetters(ciphered_word, symbol):
    return [symbol[1] if x == symbol[0] else x for x in ciphered_word]


def createMatrix(alphabet):
    return [alphabet[0:5], alphabet[5:10], alphabet[10:15], alphabet[15:20], alphabet[20:25]]


def findlocation(matrix, char):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == char:
                return str(row + 1) + str(column + 1)


def decypherWord(matrix, word):
    buffer = ""
    print("What")
    print(str(word) + " " + str(len(word)))
    for x in range(0, len(word)):
        buffer += matrix[int(str(word[x])[0]) - 1][int(str(word[x])[1]) - 1]
    return buffer


def cypher_old(word, key, matrix):
    x: str
    ciphered_message = list()
    ciphered_key = list()
    for x in word:
        ciphered_message.insert(len(ciphered_message), int(findlocation(matrix, x)))
    print(ciphered_message)
    for x in key:
        ciphered_key.insert(len(ciphered_key), int(findlocation(matrix, x)))

    print(ciphered_key)
    nihi_list = list()
    for x in range(0, len(ciphered_message)):
        nihi_list.insert(len(nihi_list), ciphered_message[x] + ciphered_key[x % len(ciphered_key)])
    return nihi_list


def decypher(cyph_word, key, matrix):  # todo rename all defs (.this = prepare decipher or sth)
    cyph_key = list()
    decyph_location = list()
    for x in key:
        cyph_key.insert(len(cyph_key), int(findlocation(matrix, x)))  # [aa,bb,cc...]
    for x in range(0, len(cyph_word)):
        decyph_location.insert(len(decyph_location),
                               cyph_word[x] - cyph_key[x % len(cyph_key)])  ##[aa,bb,cc...] po odjęciu
    decyph_word = decypherWord(matrix, decyph_location)
    return decyph_word


# nie podminiliem liter w tym kluczu

if __name__ == '__main__':
    global symbol
    word = raw_input("(OPTIONAL)Enter a word:")
    print("Ciphering the matrix with \"" + word + "\".")
    new_alphabet = modifyAlphabet(alphabet, word)
    print(str(new_alphabet) + str(len(new_alphabet)))
    print(symbol)
    word = raw_input("Enter ciphered word:")
    word = substituteLetters(word, symbol)
    print(word)
    matrix = createMatrix(new_alphabet)
    print(matrix)
    key = raw_input("Enter key:")
    key = substituteLetters(key, symbol)
    cyphered = cypher_old(word, key, matrix)
    print(cyphered)
    decyphered = decypher(cyphered, key, matrix)
    print(decyphered)


    # f_out = open("ciphered.txt", "w+")
    # f_in = open("tocipher.txt", "r")
    # f_in_buffer = f_in.readlines()
    # for x in f_in_buffer:
    #     f_out.write(cypher(list(x), key, matrix))
    #

#zamien wszystko na wielkie litery, usun spacje i znaki interpunkcyjne, wyrzuć polskie znaki

# slowo 1
# losuj symbol
# klucz
# substitute oba
# cypher
