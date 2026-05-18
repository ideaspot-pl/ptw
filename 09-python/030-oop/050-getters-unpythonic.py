class AnalyzedText:
    """
    Base class for text analysis.
    """
    text: str

    def __init__(self, text: str):
        self.text = text

    def get_words_count(self) -> int:
        return len(self.text.split())

    def get_letters_count(self) -> int:
        return len(self.text)

if __name__ == "__main__":
    cupcake = AnalyzedText("Croissant donut sesame snaps ice cream jelly beans chocolate. Powder chupa chups cotton candy ice cream gummi bears ice cream gingerbread halvah halvah. Oat cake dragée jujubes liquorice jelly macaroon jelly cake lemon drops. Gummi bears bonbon gingerbread macaroon tart cake cake.")
    print(cupcake.text)
    print("Words count:", cupcake.get_words_count())
    print("Letter count:", cupcake.get_letters_count())
