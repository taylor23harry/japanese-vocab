import datetime

class Item:
    def __init__(self, furigana, hiragana, definition):
        self.furigana = furigana
        self.hiragana = hiragana
        self.definition = definition
        self.date_added = datetime.datetime.now()

class Noun(Item):
    def __init__(self, word, furigana, hiragana, definition):
        super().__init__(word, furigana, hiragana, definition)

class Verb(Item):
    def __init__(self, stem, furigana, hiragana, definition, inflections):
        super().__init__(stem, furigana, hiragana, definition)
        self.inflections = inflections

class Particle(Item):
    def __init__(self, furigana, hiragana, definition):
        super().__init__(furigana, hiragana, definition)