from unidecode import unidecode
<<<<<<< HEAD
import pandas as pd
=======

>>>>>>> back prolly finished, working on front

class Back:
    def __init__(self):
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u",
                         "v", "w",
                         "x", "y", "z"]
        self.key = ""
<<<<<<< HEAD
<<<<<<< HEAD
        self.substitute_symbol = ("v", "w")
=======
        self.substitute_symbol = []
>>>>>>> back prolly finished, working on front
=======
        self.substitute_symbol = ("v", "w")
>>>>>>> oh my god, cyphering works <3
        self.fromfile = bool()
        self.word = ""
        self.cypher_word = ""
        self.matrix = [[]]
<<<<<<< HEAD
        self.matrix_parsed=""
        self.cyphered_key=[]
        self.cyphered_word=""
=======
>>>>>>> back prolly finished, working on front

    def setFromfile(self, x):
        self.fromfile = x

    def setSubstitute(self, sub):
        self.substitute_symbol = sub

    def substituteLetters(self, word):
        return [self.substitute_symbol[1] if x == self.substitute_symbol[0] else x for x in word]

    def removeDuplicates(self, word):
<<<<<<< HEAD
<<<<<<< HEAD
        return list(dict.fromkeys(word))
=======
        unique = []
        for elem in word:
            if elem not in unique:
                unique.append(elem)
        return unique
>>>>>>> back prolly finished, working on front
=======
        return list(dict.fromkeys(word))
>>>>>>> oh my god, cyphering works <3

    def findlocation(self, matrix, char):
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == char:
                    return str(row + 1) + str(column + 1)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> oh my god, cyphering works <3
    def prepare(self, x, is_alphabet):
        x = [x.lower() for x in x]
        x = ''.join(filter(str.isalpha, x))
        x = unidecode(x)
        x = self.substituteLetters(x)
<<<<<<< HEAD

        if is_alphabet:
            x = self.removeDuplicates(x)  # cos zes tu logicznie spieprzyl, drzemka i popraw
            return [x[0:5], x[5:10], x[10:15], x[15:20], x[20:25]]
        return x

    def formatMatrix(self,matrix):
        mat=pd.DataFrame(matrix,columns=[1,2,3,4,5],index=[1,2,3,4,5])
        mat=mat.to_string()
        self.matrix_parsed=mat

    def cipher(self, key, matrixword, word):
        self.key = self.prepare(key, False)
        self.matrix = self.prepare((list(matrixword) + self.alphabet), True)
        self.word = self.prepare(word, False)
        print(self.substitute_symbol)
        self.formatMatrix(self.matrix)
        x: str
        ciphered_message = list()
        ciphered_key = list()
        for x in self.word:
            ciphered_message.insert(len(ciphered_message), int(self.findlocation(self.matrix, x)))
        for x in self.key:
            ciphered_key.insert(len(ciphered_key), int(self.findlocation(self.matrix, x)))
        self.cyphered_key=ciphered_key
        self.cyphered_word=ciphered_message
        nihi_list = list()
        for x in range(0, len(ciphered_message)):
            nihi_list.insert(len(nihi_list), (ciphered_message[x] + ciphered_key[x % len(ciphered_key)]) % 100)
        for x in range(0, len(nihi_list)):
            if nihi_list[x] < 10:
                nihi_list[x] = "0" + str(nihi_list[x])
            else:
                nihi_list[x] = str(nihi_list[x])
        return nihi_list

    def decypherWord(self, matrix, word):
        try:
            buffer = ""
            for x in range(0, len(word)):
                buffer += matrix[int(str(word[x])[0]) - 1][int(str(word[x])[1]) - 1]
            return buffer
        except:
            return "WRONG KEY AND/OR SUBSTITUTE.\nLETTERS OUT OF BOUNDS"

    def decipher(self, key, cyph_word, matrixword):
        self.matrix = self.prepare((list(matrixword) + self.alphabet), True)
        self.key = self.prepare(key, False)
        print(self.substitute_symbol)
        print(self.matrix)
        print(self.key)
        cyph_key = list()
        decyph_location = list()
        cyph_word = cyph_word.split()
        for x in range(0, len(cyph_word)):
            y = int(cyph_word[x])
            if y < 10:
                y += 100
            cyph_word[x] = y
        self.formatMatrix(self.matrix)
        for x in self.key:
            cyph_key.insert(len(cyph_key), int(self.findlocation(self.matrix, x)))

        self.cyphered_key = cyph_key
        self.cyphered_word =  cyph_word
        for x in range(0, len(cyph_word)):
            decyph_location.insert(len(decyph_location),cyph_word[x] - cyph_key[x % len(cyph_key)])  ##[aa,bb,cc...] po odjęciu
        print(cyph_key)
        print(decyph_location)
        decyph_word = self.decypherWord(self.matrix, decyph_location)
=======
    def prepare(self, word, is_alphabet):
        word = word.lower()
        word = ''.join(filter(str.isalpha, word))
        word = unidecode(word)
        word = self.substituteLetters(word)
=======
>>>>>>> oh my god, cyphering works <3

        if is_alphabet:
            x = self.removeDuplicates(x)  # cos zes tu logicznie spieprzyl, drzemka i popraw
            return [x[0:5], x[5:10], x[10:15], x[15:20], x[20:25]]
        return x

    def cipher(self, key, matrixword, word, fromfile, filepath):
        if fromfile:
            file = open(filepath, "r")
            self.word = file.read()
        self.key = self.prepare(key, False)
        self.matrix = self.prepare((list(matrixword) + self.alphabet), True)
        self.word=self.prepare(word,False)
        x: str
        ciphered_message = list()
        ciphered_key = list()
        for x in self.word:
            ciphered_message.insert(len(ciphered_message), int(self.findlocation(self.matrix, x)))
        for x in self.key:
            ciphered_key.insert(len(ciphered_key), int(self.findlocation(self.matrix, x)))
        nihi_list = list()
        for x in range(0, len(ciphered_message)):
            nihi_list.insert(len(nihi_list), (ciphered_message[x] + ciphered_key[x % len(ciphered_key)])%100)
        for x in range(0,len(nihi_list)):
            if nihi_list[x]<10:
                nihi_list[x]="0"+str(nihi_list[x])
            else:
                nihi_list[x]=str(nihi_list[x])
        return nihi_list


<<<<<<< HEAD
    def decipher(self, key, cyph_word, matrix,fromfile, filepath):
        key = self.prepare(key, False)
        if fromfile:
            file=open(filepath,"r")
            cyph_word=file.read()
        cyph_key = list()
        decyph_location = list()
        for x in key:
            cyph_key.insert(len(cyph_key), int(self.findlocation(matrix, x)))  # [aa,bb,cc...]
        for x in range(0, len(cyph_word)):
            decyph_location.insert(len(decyph_location),
                                   cyph_word[x] - cyph_key[x % len(cyph_key)])  ##[aa,bb,cc...] po odjęciu
        decyph_word = self.decypherWord(matrix, decyph_location)
>>>>>>> back prolly finished, working on front
        return decyph_word
=======
def decypherWord(self, matrix, word):
    buffer = ""
    for x in range(0, len(word)):
        buffer += matrix[int(str(word[x])[0]) - 1][int(str(word[x])[1]) - 1]
    return buffer


def decipher(self, key, cyph_word, matrix, fromfile, filepath):
    key = self.prepare(key, False)
    if fromfile:
        file = open(filepath, "r")
        cyph_word = file.read()
    cyph_key = list()
    decyph_location = list()
    for x in key:
        cyph_key.insert(len(cyph_key), int(self.findlocation(matrix, x)))  # [aa,bb,cc...]
    for x in range(0, len(cyph_word)):
        decyph_location.insert(len(decyph_location),
                               cyph_word[x] - cyph_key[x % len(cyph_key)])  ##[aa,bb,cc...] po odjęciu
    decyph_word = self.decypherWord(matrix, decyph_location)
    return decyph_word
>>>>>>> oh my god, cyphering works <3
