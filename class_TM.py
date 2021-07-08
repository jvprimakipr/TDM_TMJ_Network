import pandas as pd

class TM:
    "Class for Turma da Mônica comic book"
    def __init__(self, directory):
        self.directory = directory
        self.data = pd.DataFrame({'Page': ['Page 1']})
        self.data.set_index('Page', inplace = True)

    def insert(self, inserting):
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

    def pack(self):
        pass

    def unpacl(self):
        pass
