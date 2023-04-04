
from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
       >>> wf = WordFinder("words.txt")
       235886 words read

       >>> word = wf.random()

       >>> isinstance(word, str)
       True
    """
    def __init__(self,file):
        self.file = file
        self.words = self.read_words_in_file(self.file)
        print (f"{len(self.words)} words read")

    def __repr__(self) -> str:
        return f"WordFinder(file={self.file})"

    def read_words_in_file(self,file):
        "Look through the given file and return a list of all found words"
        file = open(file, 'r')

        words = []
        for line in file:
            words.append(line)
        return words
    
    def random(self):
        "Return a random word from the list of found words"
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """A Subclass of WordFinder that ignores blank lines and comments
    
       >>> wf = SpecialWordFinder("words.txt")
       235886 words read

       >>> word = wf.random()

       >>> isinstance(word, str)
       True

       >>> word.startswith('#')
       False

       >>> len(word) > 0
       True
    """
    def __init__(self, file):
        super().__init__(file)

    def __repr__(self) -> str:
        return f"Special" + super().__repr__()
    
    def read_words_in_file(self,file):
        "Look through the given file and return a list of all found words"
        file = open(file, 'r')

        words = []
        for line in file:
            if not line.startswith('#') or len(line) > 0:
                words.append(line)
        return words