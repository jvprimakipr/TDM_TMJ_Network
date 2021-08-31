import pandas as pd

class TM:
    "Class for Turma da Mônica comic book"
    def __init__(self):
        self.data = pd.DataFrame({'Page': ['Page 1'], 'History' : None, 'Weight' : None})
        self.data.set_index('Page', inplace = True)
        self.characters = []
        self.n_characters = 0
        self.history = False
        self.n_history = -1
        self.end_history = False
        self.subdivisions = 0

    def insert(self, inserting, w = 1, scene = ''):        
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
            
        if inserting[0] != '' or (len(inserting) > 1 and inserting[1] != ''):
            # entre parênteses é o caso da contracapa da TMJ
            inserting.insert(1, w) # adicionando o peso daquela página/cena
            
        for character in inserting[2:]:
            if character not in self.characters:
                self.characters.append(character)
                self.n_characters += 1
        
        if len(inserting) > len(self.data.columns):
            while len(inserting) > len(self.data.columns):
                new_column = ['' for i in range(len(self.data))]
                self.data.insert(len(self.data.columns), f'Character {len(self.data.columns) - 1}', new_column, True)
        elif len(inserting) < len(self.data.columns):
            while len(inserting) < len(self.data.columns):
                inserting.append('')
    
        if len(self.data) == 1 and self.data.loc['Page 1'][0] == None:
            self.data.loc['Page 1'] = inserting
        else:
            self.data.loc[f'Page {len(self.data) - self.subdivisions + 1}{scene}'] = inserting
    
        return self.data

    def split_insert(self, inserting):
        w = round(1/inserting[0], 1)
        myaux = 1
        for i in range(1, len(inserting)):
            if isinstance(inserting[i], list):
                if 'end' in inserting:
                    inserting[i].insert(0, 'end')
                if 'begin' in inserting:
                    inserting[i].insert(0, 'begin')
                if myaux != 1:
                    self.subdivisions += 1
                self.insert(inserting[i], w = w, scene = f'.{myaux}')
                myaux += 1
    
    def inserts(self, multiple_inserting):
        for inserting in multiple_inserting:
            if len(inserting) > 0:
                if isinstance(inserting[0], int):
                    self.split_insert(inserting)
                else:
                    self.insert(inserting)
            else:
                self.insert(inserting)
    
    def pack(self, path):
        self.data.to_csv(path)

    def unpack(self, path):
        self.data = pd.read_csv(path,
                                index_col = 'Page',
                                keep_default_na = False)
        for row in self.data.iterrows():
            for character in row[1][2:]:
                if character != '' and character not in self.characters:
                    self.characters.append(character)
                    self.n_characters += 1
    #Acho que talvez tenha q consertar algo aqui
