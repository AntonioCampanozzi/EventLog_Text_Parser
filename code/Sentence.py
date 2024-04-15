

class Sentence:

    __form:str

    def __init__(self, form:str):
        self.__form=form

    def __str__(self):
        return f'{self.__form}'