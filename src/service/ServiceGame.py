class ServiceGame:
    def getListByPlatform(l, plataform):
        aux = []
        for i in l:
            if(i[2]==plataform):
                aux.append(i[2])
        return aux
    def getListByPublisher(l, publisher):
        aux = []
        for i in l:
            if(i[5]==publisher):
                aux.append(i[5])
        return aux