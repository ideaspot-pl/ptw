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

class ArticleText(AnalyzedText):
    @property
    def estimated_reading_time(self) -> int:
        return round(self.words_count / 200)

if __name__ == "__main__":
    cupcake = ArticleText("Croissant donut sesame snaps ice cream jelly beans chocolate. Powder chupa chups cotton candy ice cream gummi bears ice cream gingerbread halvah halvah. Oat cake dragée jujubes liquorice jelly macaroon jelly cake lemon drops. Gummi bears bonbon gingerbread macaroon tart cake cake. Pudding lemon drops wafer gingerbread bear claw. Ice cream pastry toffee apple pie gummies toffee tootsie roll. Jelly-o croissant candy pudding sesame snaps. Toffee danish chocolate cake gingerbread dessert cake tootsie roll. Croissant tootsie roll pastry tiramisu pudding carrot cake. Tootsie roll jelly beans lemon drops cookie topping. Wafer halvah tootsie roll icing powder tootsie roll pastry. Tart biscuit bonbon powder cake tootsie roll bonbon tiramisu chocolate cake. Dragée caramels candy canes dessert marshmallow caramels. Icing cookie soufflé icing sugar plum. Croissant donut sesame snaps ice cream jelly beans chocolate. Powder chupa chups cotton candy ice cream gummi bears ice cream gingerbread halvah halvah. Oat cake dragée jujubes liquorice jelly macaroon jelly cake lemon drops. Gummi bears bonbon gingerbread macaroon tart cake cake. Pudding lemon drops wafer gingerbread bear claw. Ice cream pastry toffee apple pie gummies toffee tootsie roll. Jelly-o croissant candy pudding sesame snaps. Toffee danish chocolate cake gingerbread dessert cake tootsie roll. Croissant tootsie roll pastry tiramisu pudding carrot cake. Tootsie roll jelly beans lemon drops cookie topping. Wafer halvah tootsie roll icing powder tootsie roll pastry. Tart biscuit bonbon powder cake tootsie roll bonbon tiramisu chocolate cake. Dragée caramels candy canes dessert marshmallow caramels. Icing cookie soufflé icing sugar plum. Croissant donut sesame snaps ice cream jelly beans chocolate. Powder chupa chups cotton candy ice cream gummi bears ice cream gingerbread halvah halvah. Oat cake dragée jujubes liquorice jelly macaroon jelly cake lemon drops. Gummi bears bonbon gingerbread macaroon tart cake cake. Pudding lemon drops wafer gingerbread bear claw. Ice cream pastry toffee apple pie gummies toffee tootsie roll. Jelly-o croissant candy pudding sesame snaps. Toffee danish chocolate cake gingerbread dessert cake tootsie roll. Croissant tootsie roll pastry tiramisu pudding carrot cake. Tootsie roll jelly beans lemon drops cookie topping. Wafer halvah tootsie roll icing powder tootsie roll pastry. Tart biscuit bonbon powder cake tootsie roll bonbon tiramisu chocolate cake. Dragée caramels candy canes dessert marshmallow caramels. Icing cookie soufflé icing sugar plum.")
    print(cupcake.text)
    print("Words count:", cupcake.words_count)
    print("Reading time:", cupcake.estimated_reading_time, "min")
