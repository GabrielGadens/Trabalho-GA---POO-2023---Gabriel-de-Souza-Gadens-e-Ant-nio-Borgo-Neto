class Troca():
    def __init__(self,nomeProponente,figReq,figDisp,status,nomeSolicitante):
        self.__nomeProponente = nomeProponente
        self.__figReq = int(figReq)
        self.__figDisp = int(figDisp)      
        self.__status = int(status)  
        self.__nomeSolicitante = nomeSolicitante

    def mostrarTroca(self):
        print('Usuário:',self.__nomeSolicitante,'quer trocar sua figurinha:',self.__figReq,'pela figurinha',self.__figDisp,'dele')

    def salvamentoTroca(self):
        texto= str(str(self.__nomeProponente)+","+str(self.__figReq)+","+str(self.__figDisp)+","+str(self.__status)+","+str(self.__nomeSolicitante)+'\n')
        f = open('Troca.csv', 'a')
        f.write(texto)
        f.close()
    
    def nomeProponente(self):
        return self.__nomeProponente
    
    def alteraStatus(self,status):
        self.__status=status

    def getStatus(self):
        return self.__status

    def getFigReq(self):
        return self.__figReq
    
    def getFigDisp(self):
        return self.__figDisp
    
    def getSolicitante(self):
        return self.__nomeSolicitante
    