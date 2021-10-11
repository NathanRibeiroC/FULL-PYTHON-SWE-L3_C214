from src.utils.csvUtils import CsvOperations

class ServiceGame:
    def getListByPlatform(l, plataform):
        aux = []
        for i in l:
            if(i[2]==plataform):
                aux.append(i)
        CsvOperations().createFile(aux)
        return aux
    def getListByPublisher(l, publisher):
        aux = []
        for i in l:
            if(i[5]==publisher):
                aux.append(i)
        CsvOperations().createFile(aux)
        return aux
    def getListByPlatformAndPublisher(l,publisher,platform):
        aux = []
        for i in l:
            if((i[5]==publisher)and(i[2]==platform)):
                aux.append(i)
        CsvOperations().createFile(aux)
        return aux