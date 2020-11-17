class isPangram:
    def game(self, word):
        litery = "abcdefghijklmnopqrstuvwxyz"
        alfa = set(litery)
        if set(word.lower()) >= alfa:
            return "True"
        elif set(word.lower())< alfa:
            return "False"
        else:
            raise Exception("Error in isPangram")