import pandas as pd

class TM:
    "Class for Turma da Mônica comic book"
    def __init__(self):
        self.data = pd.DataFrame({'Page': ['Page 1']})
        self.data.set_index('Page', inplace = True)
        self.characters = []
        self.n_characters = 0

    def insert(self, inserting):
        for character in inserting:
            if character not in self.characters:
                self.characters.append(character)
                self.n_characters += 1
        
        if len(inserting) > len(self.data.columns):
            while len(inserting) > len(self.data.columns):
                new_column = ['' for i in range(len(self.data))]
                self.data.insert(len(self.data.columns), f'Character {len(self.data.columns) + 1}', new_column, True)
        elif len(inserting) < len(self.data.columns):
            while len(inserting) < len(self.data.columns):
                inserting.append('')
    
        if len(self.data) == 1 and self.data.loc['Page 1'][0] == '':
            self.data.loc['Page 1'] = inserting
        else:
            self.data.loc[f'Page {len(self.data) + 1}'] = inserting
    
        return self.data

    def inserts(self, multiple_inserting):
        for inserting in multiple_inserting:
            self.insert(inserting)
    
    def pack(self, path):
        self.data.to_csv(path)

    def unpack(self, path):
        self.data = pd.read_csv(path,
                                index_col = 'Page',
                                keep_default_na = False)
        for row in self.data.iterrows():
            for character in row[1]:
                if character != '' and character not in self.characters:
                    self.characters.append(character)
                    self.n_characters += 1
