from src.utils.csvUtils import CsvOperations

'''
    Class that provide search based on list generated from CSV file
'''


class ServiceGame:
    @staticmethod
    def get_list_by_platform(lista, plataform):
        aux = []
        for i in lista:
            if i[2] == plataform:  # index that refeers to searched label platform
                aux.append(i)
        CsvOperations().create_file(aux)  # create file from searched file
        return aux

    @staticmethod
    def get_list_by_publisher(lista, publisher):
        aux = []
        for i in lista:
            if i[5] == publisher:
                aux.append(i)
        CsvOperations().create_file(aux)
        return aux

    @staticmethod
    def get_list_by_platform_and_publisher(lista, publisher, platform):
        aux = []
        for i in lista:
            if (i[5] == publisher) and (i[2] == platform):
                aux.append(i)
        CsvOperations().create_file(aux)
        return aux

