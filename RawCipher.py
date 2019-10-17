import random

from pip._vendor.distlib.compat import raw_input

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w",
            "x", "y", "z"]


def removeLetter(alphabet):
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


#
# def substituteLetters(ciphered_word):
#     a=[symbol if x==]
#     return ciphered_word

if __name__ == '__main__':
    word = raw_input("(OPTIONAL)Enter a word:")
    print("Ciphering the matrix with \"" + word + "\".")
    modifyAlphabet(alphabet, word)
