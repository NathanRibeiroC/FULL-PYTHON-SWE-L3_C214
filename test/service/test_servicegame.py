import pytest
from  src.utils.csvUtils import CsvOperations
from  src.service.ServiceGame import ServiceGame

@pytest.fixture
def set_csv_df():
    df = CsvOperations().csvConvert()
    return df

def test_getListByPlatformPS4(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.getListByPlatform(l,'PS4')
    assert len(ls) == 5

def test_getListByPlatformX360(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.getListByPlatform(l,'X360')
    assert len(ls) == 16

def test_getListByPublisherMicro(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.getListByPublisher(l,'Microsoft Game Studios')
    assert len(ls) == 6

def test_getListByPublisherAct(set_csv_df):
    l = set_csv_df
    ls = ServiceGame.getListByPublisher(l,'Activision')
    assert len(ls) == 14



