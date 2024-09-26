#Задача "Найдёт везде"
from pprint import pprint

class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding = 'utf-8') as file:
                line_list = []
                for line in file:
                    line = line.lower()
                    mapping = str.maketrans(",=!?;:—", '       ')
                    line = line.translate(mapping)
                    line = line.replace('  ', ' ')
                    line = line.replace('. ', ' ')
                    line = line.replace('.\n', '\n')
                    line_list.extend(line.split())
                all_words[file_name] = line_list
        return all_words

    def find(self, word):
        current_word = {}
        for name, words in self.get_all_words().items():
            for element in words:
                if word.lower() == element.lower():
                    current_word[name] = words.index(element) + 1
                    break
        return current_word

    def count(self, word):
        current_word_2 = {}
        for name, words in self.get_all_words().items():
            count = 0
            for element in words:
                if word.lower() == element.lower():
                    count +=1
            current_word_2[name] = count
        return current_word_2

