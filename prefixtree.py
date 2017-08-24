WordKey = '\n'  # any character not 'a'..'z'
def traverse(d, prefix):
    """Recursively generate all words in the Prefix Tree."""
    for k in d:
        if k == WordKey:
            yield prefix
        else:
            for _ in traverse(d[k], prefix + k):
                yield _
class PrefixTree:
    def __init__(self, *start):
        """Demonstrate prefix tree in Python give strings."""
        self.head = {}
        self.count = 0
        self.numDictionaries = 1
        for _ in start:
            self.add(_.lower())
    def add(self, value):
        """Add value to prefix tree"""
        d = self.head
        while len(value) > 0:
            if value[0] not in d:
                d[value[0]] = {}
                self.numDictionaries += 1

            d = d[value[0]]
            value = value[1:]


        if WordKey in d:
            return False
        d[WordKey] = True
        return True
    def __contains__(self, value):
        """determine if value is in prefix tree."""
        d = self.head
        while len(value) > 0:
            c = value[0]
            if c not in d:
                return False

            d = d[c]
            value = value[1:]
        return WordKey in d
    def __iter__(self):
        pass
    def __repr(self):
        pass
