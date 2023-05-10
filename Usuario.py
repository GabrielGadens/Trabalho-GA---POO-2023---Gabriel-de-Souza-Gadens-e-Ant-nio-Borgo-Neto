from Album import *
class Usuario():
    def __init__(self):
        self.__nomeDeUsuario=str('')
        self.__senha=str('')
        self.__album=Album(self)

    def getNomeDeUsuario(self):
        return self.__nomeDeUsuario
    
    def cadastrar(self,nomeDeUsuario,senha):
        self.__nomeDeUsuario=nomeDeUsuario
        self.__senha=senha
    
    def verificaLogin(self,nomeDeUsuario,senha):
        if self.__nomeDeUsuario==nomeDeUsuario and self.__senha==senha:
            return True
        else:
            return False
    
    def getAlbum(self):
        return self.__album
    
    def salvamento(self):
        texto= str(self.__nomeDeUsuario+","+self.__senha+'\n')
        print(texto)
        f = open('Usuarios.csv', 'a')
        f.write(texto)
        f.close()