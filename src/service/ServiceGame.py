"""Module used into searches"""
from src.utils.csvUtils import CsvOperations

class ServiceGame:
    """Class that provides search services into csv list based"""
    @staticmethod
    def get_list_by_platform(lista, plataform):
        """Search games based on a platform"""
        aux = []
        for i in lista:
            if i[2] == plataform:  # index that refeers to searched label platform
                aux.append(i)
        CsvOperations().create_file(aux)  # create file from searched file
        return aux

    @staticmethod
    def get_list_by_publisher(lista, publisher):
        """Search games based on a publisher"""
        aux = []
        for i in lista:
            if i[5] == publisher:
                aux.append(i)
        CsvOperations().create_file(aux)
        return aux

    @staticmethod
    def get_list_by_platform_and_publisher(lista, publisher, platform):
        """Search games based on platform and publisher"""
        aux = []
        for i in lista:
            if (i[5] == publisher) and (i[2] == platform):
                aux.append(i)
        CsvOperations().create_file(aux)
        return aux
