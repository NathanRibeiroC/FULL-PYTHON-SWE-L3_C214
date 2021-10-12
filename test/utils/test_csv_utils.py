from src.utils.csvUtils import CsvOperations
import os
from pathlib import Path
# test if csvConvert function returns list object
def test_csvConvert():
    df = CsvOperations().csv_convert()
    assert str(type(df)) == "<class 'list'>"

def test_fileCreated():

    aux = [['16', 'Kinect Adventures!', 'X360', '2010', 'Misc', 'Microsoft Game Studios', '14.97', '4.94', '0.24', '1.67', '21.82']]
    CsvOperations.create_file(aux)
    FILE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/src/resources/csv_searched_games.csv'
    my_file = Path(FILE_DIR)
    if my_file.is_file():
        assert True
    else:
        assert False





