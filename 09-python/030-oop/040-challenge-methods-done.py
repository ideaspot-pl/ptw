class AnalyzedText:
    """
    Base class for text analysis.
    """
    text: str

    def __init__(self, text: str):
        self.text = text

    def count_words(self) -> int:
        return len(self.text.split())

    def count_letters(self) -> int:
        return len(self.text)

if __name__ == "__main__":
    cupcake = AnalyzedText("Croissant donut sesame snaps ice cream jelly beans chocolate. Powder chupa chups cotton candy ice cream gummi bears ice cream gingerbread halvah halvah. Oat cake dragée jujubes liquorice jelly macaroon jelly cake lemon drops. Gummi bears bonbon gingerbread macaroon tart cake cake.")
    print(cupcake.text)
    print("Words count:", cupcake.count_words())
    print("Letter count:", cupcake.count_letters())
