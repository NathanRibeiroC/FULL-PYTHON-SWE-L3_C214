"""This module provides a class to handle with csv files"""
import os
import csv
import pandas as pd


class CsvOperations:
    """Class that abstract all operations related to csv"""
    def __init__(self) -> None:
        """Csv initializator (sets default path for csv reference file)"""
        self.filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))\
                        + '/resources/'    # parent do diretório atual + folder recources

    # convert csv data to list
    def csv_convert(self):
        """Convert csv to list"""
        df_csv = pd.read_csv(self.filepath
                         +'vendas-games.csv')  # read csv and parse into pandas DataFrame
        df_list = df_csv.values.tolist()  # from pandas Data Frame to dict list
        return df_list

    # create file on given directory
    @staticmethod
    def create_file(aux):
        """Create csv file based on search"""
        file_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) \
            + '/src/resources/csv_searched_games.csv'  # path where file will be created

        # column names of csv file generated
        fields = ["rank", "name", "platform", "year", "genre", "publisher"
            , "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales"]

        with open(file_dir, 'w') as file:
            # using csv.writer method from CSV package
            write = csv.writer(file)
            write.writerow(fields)
            write.writerows(aux)
