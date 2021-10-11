import pandas as pd
import os
import csv

'''
    Class that abstract all operations related to csv
'''


class CsvOperations:
    def __init__(self) -> None:
        self.filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))\
                        + '\\resources\\'    # parent do diretório atual + folder recources

    # convert csv data to list
    def csv_convert(self):
        df = pd.read_csv(self.filepath+'vendas-games.csv')  # read csv and parse into pandas DataFrame
        df_list = df.values.tolist()  # from pandas Data Frame to dict list
        return df_list

    # create file on given directory
    @staticmethod
    def create_file(aux):

        file_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) \
            + '\\src\\resources\\csv_searched_games.csv'  # path where file will be created

        fields = ["rank", "name", "platform", "year", "genre", "publisher", "na_sales", "eu_sales", "jp_sales",
                  "other_sales", "global_sales"]    # column names of csv file generated

        with open(file_dir, 'w') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(aux)
