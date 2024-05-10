from EventLog_Text_Parser.code.Paragraph import Paragraph
import pickle


class Text:
    __paragraphSet: list

    def __init__(self):
        self.__paragraphSet = []

    def add(self, paragraph: Paragraph):
        self.__paragraphSet.append(paragraph)

    def store(self, filepath: str, filetype: str = '.pickle'):
        if filetype == '.pickle':
            file = open(f'{filepath}.PICKLE', 'wb')
            pickle.dump(self, file)
            file.close()
        elif filetype == '.txt':
            file = open(f'{filepath}.txt', 'w')
            file.write(self.__str__())
            file.close()

    @staticmethod
    def retrieve(filepath: str):
        file = open(f'{filepath}.PICKLE', 'rb')
        depickledtext: Text = pickle.load(file)
        file.close()
        return depickledtext

    def getParagraphSet(self):
        return self.__paragraphSet

    def getParagraph(self, pargfIndex: int):
        return self.__paragraphSet[pargfIndex]

    def extractLabels(self):
        labels = []
        for par in self.__paragraphSet:
            labels.append(par.getClass())
        return labels

    def uniqueLabels(self):
        labels = []
        for par in self.__paragraphSet:
            labels.append(par.getClass())
        return list(set(labels))

    def __str__(self):
        textstr = ''
        for paragraph in self.__paragraphSet:
            textstr += f'{paragraph}\n'
        return textstr

    def __len__(self, metric: str = 'characters'):
        traceLens = []
        for i in self.__paragraphSet:
            traceLens.append(i.__len__(metric))

        return traceLens
