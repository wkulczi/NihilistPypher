class Back:
    def __init__(self, key, martix_word, cypher_word, substitute_choice):
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u",
                         "v", "w",
                         "x", "y", "z"]
        self.key = key
        self.substitutes = []
        self.word = martix_word
        self.cypher_word = cypher_word
        self.substitute_choice = substitute_choice


