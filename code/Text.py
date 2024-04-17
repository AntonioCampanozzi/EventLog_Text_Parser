from EventLog_Text_Parser.code.Paragraph import Paragraph


class Text:
    paragraphSet: list = []

    def add(self, paragraph: Paragraph):
        self.paragraphSet.append(paragraph)

    def store(self, filepath: str):
        with open(filepath, 'w') as file:
            file.write(self.__str__())

    def __str__(self):
        textstr = ''
        for paragraph in self.paragraphSet:
            textstr += f'{paragraph}\n'
        return textstr
