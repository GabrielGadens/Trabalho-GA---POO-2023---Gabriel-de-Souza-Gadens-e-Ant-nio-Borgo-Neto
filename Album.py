from Usuario import *
class Album():
    def __init__(self,usuario):
        self.__usuario=usuario
        self.__figurinhas=[]
        self.__requisicoesTrocas=[]
    
    
    def insereFigurinha(self,figurinha):
        self.__figurinhas.append(figurinha)
    
    def insereRequisicoesDeTroca(self,troca):
        self.__requisicoesTrocas.append(troca)
    
    def getFigurinhas(self):
        return self.__figurinhas
    
    def getRequisicoesDeTroca(self):
        return self.__requisicoesTrocas
    
    def getUsuario(self):
        return self.__usuario
    
    def carregaFigurinhas(self,figurinhas):
        self.__figurinhas=figurinhas
        