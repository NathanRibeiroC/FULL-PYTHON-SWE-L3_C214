"""test_csv_utils.py has as focus testing csvUtils class"""
import os
from pathlib import Path
from src.utils.csvUtils import CsvOperations

def test_csv_convert():
    """Test if method returns a type <class 'list'> object"""
    df_list = CsvOperations().csv_convert()
    assert str(type(df_list)) == "<class 'list'>"

def test_file_created():
    """Test if csv file was created"""
    aux = [['16', 'Kinect Adventures!', 'X360', '2010', 'Misc'
               , 'Microsoft Game Studios', '14.97', '4.94', '0.24', '1.67', '21.82']]
    CsvOperations.create_file(aux)
    file_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))\
               +'/src/resources/csv_searched_games.csv'
    my_file = Path(file_dir)
    if my_file.is_file():
        assert True
    else:
        assert False
