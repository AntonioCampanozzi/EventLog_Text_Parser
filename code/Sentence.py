class Sentence:
    __form: str

    def __init__(self, form: str):
        self.__form = form

    def __str__(self):
        s = ''
        s += f'{self.__form}'
        return s

    def __len__(self, metric: str = 'characters'):

        sentenceLen = 0

        if metric == 'words':
            # sentence length in this case equals to the number of words it has.
            sentenceLen = self.__form.strip().split(' ').__len__()

        elif metric == 'characters':
            # sentence length in this case equals to the number of characters it has.
            sentenceLen = self.__form.replace(' ', '').__len__()

        return sentenceLen
