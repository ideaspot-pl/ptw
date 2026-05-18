class AnalyzedText:
    """
    Base class for text analysis.
    """
    __text: str

    def __init__(self, text: str):
        self.__text = text

    @property
    def words_count(self) -> int:
        return len(self.__text.split())

    @property
    def letters_count(self) -> int:
        return len(self.__text)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    @property
    def word_histogram(self) -> dict[str, int]:
        histogram = {}
        for token in sorted(self.__text.lower().split()):
            token = token.strip(',.?!";()')
            if token in histogram:
                histogram[token] += 1
            else:
                histogram[token] = 1
        return histogram
