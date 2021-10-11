import pandas as pd
import os
import csv

class CsvOperations:
    def __init__(self) -> None:
        self.filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))+'\\resources\\'    # parent do diretório atual + folder recources

    def csvConvert(self):
        df = pd.read_csv(self.filepath+'vendas-games.csv') # read csv and parse into pandas DataFrame
        l = df.values.tolist() # from pandas Data Frame to dict list
        return(l)

    def createFile(self,aux):
        FILE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '\\src\\resources\\csv_searched_games.csv'
        fields = ["rank","name","platform","year","genre","publisher","na_sales","eu_sales","jp_sales","other_sales","global_sales"]
        with open(FILE_DIR, 'w') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(aux)
