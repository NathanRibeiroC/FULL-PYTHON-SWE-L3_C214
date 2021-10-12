"""test_servicegame.py have as focus testing ServiceGame class"""
import pytest
from src.utils.csvUtils import CsvOperations
from src.service.ServiceGame import ServiceGame

@pytest.fixture(name="set_csv_df")
def fixture_set_csv_df():
    """From csv file, define a list"""
    df_list = CsvOperations().csv_convert()
    return df_list

def test_get_list_by_platform_ps4(set_csv_df):
    """Test how many games have PS4 as platform"""
    list_csv = set_csv_df
    lsearched_csv = ServiceGame.get_list_by_platform(list_csv, 'PS4')
    assert len(lsearched_csv) == 5

def test_get_list_by_platform_x360(set_csv_df):
    """Test how many games have X360 as platform"""
    list_csv = set_csv_df
    lsearched_csv = ServiceGame.get_list_by_platform(list_csv, 'X360')
    assert len(lsearched_csv) == 16

def test_get_list_by_publisher_micro(set_csv_df):
    """Test how many games were published by Microsoft Game Studios"""
    list_csv = set_csv_df
    lsearched_csv = ServiceGame.get_list_by_publisher(list_csv, 'Microsoft Game Studios')
    assert len(lsearched_csv) == 6

def test_get_list_by_publisher_act(set_csv_df):
    """Test how many games were published by Activision"""
    list_csv = set_csv_df
    lsearched_csv = ServiceGame.get_list_by_publisher(list_csv, 'Activision')
    assert len(lsearched_csv) == 14

def test_get_list_by_publisher_and_platform(set_csv_df):
    """Test if in cases where Publisher and Platform are searched togheter,
    the list returns right value"""
    list_csv = set_csv_df
    lsearched_csv = ServiceGame.get_list_by_platform_and_publisher(list_csv, 'Nintendo', 'Wii')
    assert (lsearched_csv[0][5] == 'Nintendo') and (lsearched_csv[0][2] == 'Wii')
