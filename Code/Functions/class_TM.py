import pandas as pd

class TM:
    "Class for Turma da Mônica comic book"
    def __init__(self):
        self.data = pd.DataFrame({'Page': ['Page 1'], 'History' : None})
        self.data.set_index('Page', inplace = True)
        self.characters = []
        self.n_characters = 0
        self.history = False
        self.n_history = -1
        self.end_history = False

    def insert(self, inserting):
        if 'begin' in inserting:
            self.n_history += 1
            self.history = True
            inserting.remove('begin')
            
        if 'end' in inserting:
            self.end_history = True
            inserting.remove('end')
        
        if self.history and self.n_history > 0:
            inserting.insert(0, self.n_history)
        elif self.history:
            inserting.insert(0, 'Capa')
        else:
            inserting.insert(0, '')

        if self.end_history:
            self.history = False
            self.end_history = False
            
        for character in inserting:
            if character not in self.characters and type(character) != int:
                self.characters.append(character)
                self.n_characters += 1
        
        if len(inserting) > len(self.data.columns):
            while len(inserting) > len(self.data.columns):
                new_column = ['' for i in range(len(self.data))]
                self.data.insert(len(self.data.columns), f'Character {len(self.data.columns)}', new_column, True)
        elif len(inserting) < len(self.data.columns):
            while len(inserting) < len(self.data.columns):
                inserting.append('')
    
        if len(self.data) == 1 and self.data.loc['Page 1'][0] == None:
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
