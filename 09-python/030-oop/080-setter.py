class AnalyzedText:
    """
    Base class for text analysis.
    """
    _text: str

    def __init__(self, text: str):
        self._text = text

    @property
    def words_count(self) -> int:
        return len(self._text.split())

    @property
    def letters_count(self) -> int:
        return len(self._text)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

if __name__ == "__main__":
    cupcake = AnalyzedText("Croissant donut sesame snaps ice cream jelly beans chocolate. Powder chupa chups cotton candy ice cream gummi bears ice cream gingerbread halvah halvah. Oat cake dragée jujubes liquorice jelly macaroon jelly cake lemon drops. Gummi bears bonbon gingerbread macaroon tart cake cake.")
    cupcake.text = "This is a new text"
    print(cupcake.text)     # pythonic
    print("Words count:", cupcake.words_count)
    print("Letter count:", cupcake.letters_count)
