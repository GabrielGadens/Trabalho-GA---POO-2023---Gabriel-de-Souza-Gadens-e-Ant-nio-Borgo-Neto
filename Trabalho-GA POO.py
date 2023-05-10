import csv
import random
from Usuario import *
from Figurinha import *
from Album import *           
from Troca import *
from Funcoes import *
if __name__ == '__main__':
    figurinhasTODAS=[]
    figurinhasTODAS=carregaFigurinhas()    #chama a função que vai no arquivo csv e inicia todos objetos figurinha
    figNaOrdem=[] #usamos para posteriormente mostrar as figurinhas em ordem
    podeTrocar=[]  #salva todas as figurinhas com o status disponíveis para troca =2
    reqTrocas=[] # salva as requisições de troca
    usuario=Usuario() #inicia um objeto do tipo usuário
    trocas=[]  
    trocas=carregaTrocas()   #carrega todas as trocas do csv
    menu2 = False
    escolha = int(0)
    contador = 0
    while escolha !=3 :
        print('\n   MENU\n1 - Novo Álbum\n2 - Acessar meu Álbum\n3 - Sair do Aplicativo')
        escolha = int(validaNumero())   #pega um valor com uma função de validação de números
        
        if escolha == 1 :
            usuario=criarUsuario(usuario)  
            menu2=True

        elif escolha == 2:
            usuario = ValidaLogin() #chama função que valida login
            if usuario != 0:
                menu2=True
                
            else:
                print('Login Inválido!!!')
        
        elif escolha == 3:
            print('Saindo...')

        else:
            print(' opção inválida, tente novamente... ')

        if menu2 == True: # opção destinada para o segundo menu, após login
            album=Album(usuario) #inicia um album com usuario logado como dono
            figurinhas=[]
            album.carregaFigurinhas(figurinhas) 
            print('\nBem-vindo,',usuario.getNomeDeUsuario())

            while escolha !=6 :
                podeTrocar=disponiveisParaTroca(figurinhasTODAS) #aqui armazenamos as figurinhas disponiveis para troca em um array
                figurinhas=carrefaFigurinhaLogado(usuario.getNomeDeUsuario(),figurinhasTODAS)  #pega somente as figurinhas do usuário logado
                print('   MENU\n1 - Folhear meu album\n2 - Consultar minhas figurinhas\n3 - Abrir pacote de Figurinhas \n4 - Propor troca de figurinhas \n5 - Revisar solicitações de troca\n6 - Voltar ao menu anterior')
                escolha = int(validaNumero())
                if escolha == 1:
                    for i in range (0,100):
                        figNaOrdem.append('NADA') # inserimos um valor padrão para todos as posições do album e depois atualizamos com as que o usuário tem
                    num=1
                    i=1
                    if len(figurinhas)>0:
                        for i in range(1,99):
                            for fig in figurinhas:
                                if fig.verificaNum(i) == True:
                                    if fig.consultaStatus()==0:
                                        texto=fig.getNome()+' Pode colar!!!'
                                        figNaOrdem[i-1]=texto
                                    elif fig.consultaStatus()==2:
                                        texto=fig.getNome()+' Disponibilizou para Troca!!!'
                                        figNaOrdem[i-1]=texto
                                    else:
                                        figNaOrdem[i-1]=fig.getNome()
                    i=1
                    while num!=100:
                        print(num,':',figNaOrdem[num-1])
                        if num%10 == 0:
                            print('\n1 = Próxima pág\n2 - SAIR')
                            escolha = validaNumero()
                            if escolha ==2:
                                num=99
                        num+=1
    
                elif escolha == 2:
                    if len(figurinhas)>0:
                        print('Suas Figurinhas são: ')
                        for fig in figurinhas:  #aqui percorremos todas a figurinhas do usuário logado
                            fig.mostrarFigurinha()
                        while escolha !=3 :
                            print('\n   MENU\n1 - Colar Figurinha\n2 - Disponibilizar para troca\n3 - Voltar ao Menu anterior\n')
                            escolha = int(validaNumero())
                            if escolha == 1:
                                print('Qual Número da figurinha que deseja colar?\n')
                                escolha = int(validaNumero())
                                for fig in figurinhas:
                                    if fig.verificaNum(escolha) is True:
                                        fig.colaFig() #altera o status da figurinha
                                        break

                            elif escolha == 2:
                                print('Qual Número da figurinha que deseja Trocar?\n')
                                escolha = int(validaNumero())
                                for fig in figurinhas:
                                    if fig.verificaNum(escolha) is True:
                                        fig.statusTroca() #altera o status da vigurinha
                                        break

                    else:
                        print('Você não possui figurinhas')

                elif escolha == 3:
                    for i in range(0,3):
                        numeroFig=random.randint(1,99) #utilizamos da biblioteca random para pegar número aleatório
                        nome = 'fig'+str(numeroFig)
                        pag = int((numeroFig/10)+1)
                        figurinha=Figurinha(numeroFig,nome,'chutar',pag,0,usuario.getNomeDeUsuario())
                        album.insereFigurinha(figurinha)
                        figurinha.mostrarFigurinha()
                        figurinhasTODAS.append(figurinha)
                    
                elif escolha == 4:
                    if len(podeTrocar)>0: # testamos se tem figurinhas disponiveis para troca
                        print('Figurinhas disponíveis para troca...')
                        for i in podeTrocar:
                            if i.verificaDono()!=usuario.getNomeDeUsuario() and i.consultaStatus()==2:
                                print(i.verificaDono(),'tem:')
                                i.mostrarFigurinha()
                                print()
                                contador+=1
                        if contador>0:
                            contador=0
                            print('Digite o número da figurinha que vc deseja:')
                            figRequerida=int(validaNumero())
                            for i in podeTrocar:
                                if i.verificaNum(figRequerida) == True and i.consultaStatus()==2 and i.verificaDono()!=usuario.getNomeDeUsuario():
                                    print('Digite o número da SUA figurinha que vc deseja trocar pela',figRequerida,':')
                                    figDisp=validaNumero()
                                    for x in figurinhas:
                                        if x.verificaNum(figDisp)==True :
                                            if x.consultaStatus()!=1:
                                                troca=Troca(i.verificaDono(),figRequerida,figDisp,0,usuario.getNomeDeUsuario())
                                                trocas.append(troca)
                                                troca.salvamentoTroca()
                                                print('\nRequesição de troca salva!!!\n')
                                            else:
                                                print('Sua figurinha está colada, não pode trocar...')
                                        else:
                                            contador+=1
                                            if contador==len(figurinhas):
                                                print('\nVocê não possui essa carteirinha...\n')
                        else:
                            print('\n Fim da LISTA, caso não apareceu nenhuma opção é porque não tem trocas disponíveis\n')
                    else:
                        print('\n Fim da LISTA, caso não apareceu nenhuma opção é porque não tem trocas disponíveis\n')
                elif escolha == 5:
                    contador=0
                    for i in trocas:  #percorre todas as trocas
                        if i.nomeProponente()==usuario.getNomeDeUsuario() and i.getStatus()==0:
                            contador+=1
                            i.mostrarTroca()
                            print('Você aceita?     1 - Sim   0 - Não   ou outra resposta para ver as outras solicitações')
                            aceitaTroca=int(validaNumero())
                            if aceitaTroca == 1:
                                i.alteraStatus(1)
                                figReq=i.getFigReq()
                                figDisp=i.getFigDisp()
                                for x in figurinhas:
                                    if x.verificaDono()==usuario.getNomeDeUsuario() and x.verificaNum(figReq)== True:
                                        if x.consultaStatus()!=1:
                                            salvaFig=x # salva a figurinha para que caso esteja tudo certo faça a troca de fato
                                        else:
                                            i.alteraStatus(2)
                                            print('\nTroca Negada!!! Sua figurinha foi colada\n')
                                for x in figurinhasTODAS:
                                    if x.verificaDono()==i.getSolicitante() and x.verificaNum(figDisp)==True: #verifica a figurinha disponibilizada
                                        if x.consultaStatus()!=1:
                                            x.mudaDono(usuario.getNomeDeUsuario())
                                            salvaFig.mudaDono(i.getSolicitante())
                                            print('\nTroca efetuada com sucesso!!!\n ')
                                        else:
                                            i.alteraStatus(2)
                                            print('\nTroca Negada!!! outro usuário indisponibilizou a figurinha\n')
                    
                                
                            elif aceitaTroca == 0:
                                i.alteraStatus(2)  #nega a troca
                                print('Troca Negada!!!')
                            
                    if contador==0:
                        print('\nNão tem solicitações de troca esperando por seu aceite\n')
        
                elif escolha == 6:
                    menu2=False
                else:
                    print(' opção inválida, tente novamente...')
                f = open('Figurinhas.csv', 'w') #apaga as figurinhas do arquivo
                f.write('')
                f.close()
                for fig in figurinhasTODAS: #salva as figurinhas atualizadas
                    fig.salvamentoFigurinha()
                f = open('Troca.csv', 'w') #apaga as trocas do arquivo
                f.write('')
                f.close()
                for troca in trocas: #salva as trocas atualizadas
                    troca.salvamentoTroca()