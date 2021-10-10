import pandas as pd
import os

class CsvOperations:
    def __init__(self) -> None:
        self.filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))+'\\resources\\'    # parent do diretório atual + folder recources
    
    def csvConvert(self):
        df = pd.read_csv(self.filepath+'vendas-games.csv') # read csv and parse into pandas DataFrame
        l = df.values.tolist() # from pandas Data Frame to dict list
        return(l)
