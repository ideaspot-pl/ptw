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
        # --> here!
        return histogram

if __name__ == "__main__":
    cupcake = AnalyzedText("Croissant donut sesame snaps ice cream jelly beans chocolate. Powder chupa chups cotton candy ice cream gummi bears ice cream gingerbread halvah halvah. Oat cake dragée jujubes liquorice jelly macaroon jelly cake lemon drops. Gummi bears bonbon gingerbread macaroon tart cake cake.")
    for word, count in cupcake.word_histogram.items():
        print(f"{word}: {count}")
