import csv
class Figurinha():
    def __init__(self,numero,nome,conteudo,nroPagina,status,usuario):
        self.__numero=int(numero)
        self.__nome=str(nome)
        self.__conteudo=str(conteudo)
        self.__nroPagina=int(nroPagina)
        self.__status=int(status)
        self.__nomeUsu=usuario

    def consultaStatus(self):
        return self.__status
    
    def mostrarFigurinha(self):
        if self.__status == 0 or self.__status== 2 :
            print('Nº',self.__numero,'Nome:',self.__nome,'Pag:',self.__nroPagina)

    def colaFig(self):
        if self.__status == 0:
            self.__status=1
            print('Figurinha Colada!!!')
        else:
            print('Opção não disponível')
        
    def verificaNum(self,num):
        if self.__numero == num:
            return True
        else:
            return False
        
    def getNumeroPag(self):
        return self.__nroPagina
    
    def statusTroca(self):
        if self.__status == 0:
            self.__status=2
            print('Figurinha disponível para troca!!!')
        else:
            print('Opção não disponível')
       
    def getNumero(self):
        return self.__numero
    
    def getNome(self):
        return self.__nome
    
    def salvamentoFigurinha(self):
        texto= str(str(self.__numero)+","+str(self.__nome)+","+self.__conteudo+","+str(self.__nroPagina)+","+str(self.__status)+","+str(self.__nomeUsu)+'\n')
        f = open('Figurinhas.csv', 'a')
        f.write(texto)
        f.close()

    def verificaDono(self):
        return self.__nomeUsu
    
    def mudaDono(self,novoDono):
        self.__nomeUsu=novoDono
        self.__status=0