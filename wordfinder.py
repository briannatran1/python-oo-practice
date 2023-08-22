from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Create word finder from path"""
        self.path = path
        self.list = self.generate_list()
        self.count_words_read()

    def __repr__(self):
        return f"<WordFinder path={self.path}>"

    def random(self):
        """Get random word from list"""
        return choice(self.list).replace('\n', '')

    def generate_list(self):
        """generates list from file"""
        return open(self.path).readlines()

    def count_words_read(self):
        """Print number of words read"""
        print(f"{len(self.list)} words read")


class SpecialWordFinder(WordFinder):
    """RandomWordFinder: finds words from a file (excludes comments and blank lines)"""

    def __init__(self, path):
        """get parent's initializer"""
        super().__init__(path)
        self.list = self.filter_words()

    def filter_words(self):
        new_list = []
        for word in self.list:
            if not word.startswith("\n") and not word.startswith("#"):
                new_list.append(word)
        return new_list
