class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphaToMorse = {
            "a" : ".-",
            "b" : "-...",
            "c" : "-.-.",
            "d" : "-..",
            "e" : ".",
            "f" : "..-.",
            "g" : "--.",
            "h" : "....",
            "i" : "..",
            "j" : ".---",
            "k" : "-.-",
            "l" : ".-..",
            "m" : "--",
            "n" : "-.",
            "o" : "---",
            "p" : ".--.",
            "q" : "--.-",
            "r" : ".-.",
            "s" : "...",
            "t" : "-",
            "u" : "..-",
            "v" : "...-",
            "w" : ".--",
            "x" : "-..-",
            "y" : "-.--",
            "z" : "--.."
        }

        morseTransformations = set()
        for word in words:
            morse = ''
            for c in word:
                morse += alphaToMorse[c]
            morseTransformations.add(morse)

        return len(morseTransformations)
