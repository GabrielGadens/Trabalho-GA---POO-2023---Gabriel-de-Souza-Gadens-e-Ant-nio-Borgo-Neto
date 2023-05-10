import csv
from Figurinha import *
from Usuario import *
from Troca import *

def ValidaLogin():
    f = open('Usuarios.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    x=0
    while x!=1:
        NomeUsu=str(input('Digite seu usuário: '))
        SenhaUsu=str(input('Digite sua senha: '))
        for i in range(0,len(tabela)) :
            if tabela[i][0]==NomeUsu and tabela[i][1]==SenhaUsu:
                print('logado!')
                usuario=Usuario()
                usuario.cadastrar(NomeUsu,SenhaUsu)
                return usuario
        print('\nUsuário ou senha inválidos!!! Tente novamente...\n')
                
def carregaFigurinhas():
    figurinhas=[]
    f = open('Figurinhas.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    for i in range(0,len(tabela)) :
        figurinha=Figurinha(tabela[i][0],tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4],tabela[i][5])
        figurinhas.append(figurinha)
    return figurinhas

def validaNumero ():
    while True:
        try:
            numEntrada = float(input('Digite aqui: '))
            if numEntrada>0:
                break       
            else:
                print('Não aceitamos números negativos e nem zero')
                print('Tente novamente com números válidos...')             
        except ValueError:
            print("Digite somente números!")
    return numEntrada

def criarUsuario(usuario):
    usuarioValido=False
    while usuarioValido!=True:
        nomeUsu=str(input('Digite seu usuário: '))
        senhaUsu=str(input('Digite sua senha: '))
        usuarioValido=ValidaUsuario(nomeUsu)
    usuario.cadastrar(nomeUsu,senhaUsu)
    usuario.salvamento()
    return usuario

def ValidaUsuario(nomeUsu):
    f = open('Usuarios.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    for i in range(0,len(tabela)) :
        if tabela[i][0]==nomeUsu:
            print('\nUsuário inválido\n')
            return  False
    return True                  

def carrefaFigurinhaLogado(nome,figurinhasTODAS):
    figurinhas=[]
    for i in figurinhasTODAS:
        if i.verificaDono()==nome:
            figurinhas.append(i)
    return figurinhas


def disponiveisParaTroca(figurinhasTODAS):
    podeTrocar=[]
    for i in figurinhasTODAS:
        if i.consultaStatus()==2:
            podeTrocar.append(i)
    return podeTrocar

def carregaTrocas():
    trocas=[]
    f = open('Troca.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    for i in range(0,len(tabela)) :
        troca=Troca(tabela[i][0],tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4])
        trocas.append(troca)
    return trocas