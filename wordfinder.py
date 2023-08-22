from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Create word finder from path"""
        self.path = path
        self.list = open(self.path).readlines()
        self.count_words_read()

    def __repr__(self):
        return f"<WordFinder path={self.path}>"

    def random(self):
        """Get random word from list"""
        return choice(self.list).replace('\n', '')

    # def generate_list(self):
    #     return open(self.path).readlines()

    def count_words_read(self):
        """Print number of words read"""
        print(f"{len(self.list)} words read")
