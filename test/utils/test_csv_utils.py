from  src.utils.csvUtils import CsvOperations

# test if csvConvert function returns list object
def test_csvConvert():
    df = CsvOperations().csvConvert()
    assert str(type(df)) == "<class 'list'>"



