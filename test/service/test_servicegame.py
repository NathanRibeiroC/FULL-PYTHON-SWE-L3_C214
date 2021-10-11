import pytest
from  src.utils.csvUtils import CsvOperations
from  src.service.ServiceGame import ServiceGame

@pytest.fixture
def set_csv_df():
    df = CsvOperations().csv_convert()
    return df

def test_getListByPlatformPS4(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.get_list_by_platform(l, 'PS4')
    assert len(ls) == 5

def test_getListByPlatformX360(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.get_list_by_platform(l, 'X360')
    assert len(ls) == 16

def test_getListByPublisherMicro(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.get_list_by_publisher(l, 'Microsoft Game Studios')
    assert len(ls) == 6

def test_getListByPublisherAct(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.get_list_by_publisher(l, 'Activision')
    assert len(ls) == 14

def test_getListByPublisherAndPlatform(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.get_list_by_platform_and_publisher(l, 'Nintendo', 'Wii')
    assert (ls[0][5] == 'Nintendo') and (ls[0][2] == 'Wii')



