# -*- coding: utf-8 -*-
"""
Created on Wed Sep  10 15:54:44 2019

TRABALHO DA DISCIPLINA DCC014 - INTELIGÊNCIA ARTIFICIAL

@authors: Ana Carolina Fidelis Gonçalves
         Cássio Henrique Resende Reis
         João Pedro de Souza Jardim da Costa
         João Victor Dutra Balboa
         Rian Das Dores Alves
         Yan de Paiva Andrade pinto
         
"""
#Importando as bibliotecas que serão usadas
from copy import deepcopy #Função para fazer cópia de objetos
import time #Função para calcular o tempo

#Classe que representa um nó da árvore, tendo seu estado atual,
#nível e as regras já utilizadas-----------------------------------------------------------
class No:
    
    '''Construtor: inicia todas as posições de estado com v (vazio), cria um vetor vazio de 
    regras, um vetor p/ filhos, uma variável p/ pai e o níviel é recebido como parâmetro'''
    def __init__(self, nivel): 
        self.estado = [0, 0, 0, 0] #Cada posição representa um cavalo: 0 -> branco1, 1: -> branco2, 2 -> preto1 e 3 -> preto2
        self.nivel = nivel
        self.regras = []
        self.filhos = []
        self.pai = None
        self.regraGeradora = 0
        
    #Seta o estado atual
    def setEstado(self, estado):
        self.estado = deepcopy(estado) #O estado do nó passa a ser uma cópia do estado passado como parâmetro
        
    #Retorna o estado
    def getEstado(self):
        return self.estado
    
    #Retorna o nível
    def getNivel(self):
        return self.nivel
    
    #Modifica o nível
    def setNivel(self, nivel):
        self.nivel = nivel
    
    #Retorna o objeto que ocupa aquela posição (vazio ou o cavalo correspondente)
    def checaPosicao(self, posicao):
        return self.estado[posicao]
    
    #Move o cavalo para a próxima posição possível (de acordo com a regra)
    def moveCavalo(self, cavalo, estados):
        noAux = None
        t = Transicoes() #Instancia um objeto da classe que controla as transições
        posicaoAtual = self.checaPosicao(cavalo) #Acha a posição atual do cavalo
        proximaPosicao = t.getProximo(posicaoAtual) #Acha a próxima posição possível para este
        if(proximaPosicao not in self.estado): #Se posição para qual cavalo vai andar está vazia, tenta andar
            estadoAuxiliar = deepcopy(self.estado) #Copia o estado atual p/ um auxiliar
            estadoAuxiliar[cavalo] = proximaPosicao #Move o cavalo p/ a próxima posição 
            if(estadoAuxiliar not in estados): #Se o estado auxiliar gerado ainda não apareceu nos níveis acima, passa para este estado
                noAux = No(self.nivel + 1)
                noAux.setPai(self)
                noAux.estado = deepcopy(estadoAuxiliar) #Realiza a troca de estado
                self.setFilho(noAux)
                return deepcopy(noAux)
        return noAux
    
    #Adiciona regra no vetor
    def adicionaRegra(self, regra):
        self.regras.append(regra)
        
    #Retorna as regras usadas
    def regrasUsadas(self):
        return self.regras
    
    #Remove regra do vetor
    def removeRegra(self):
        return self.regras.pop()
    
    #Seta a regra geradora do estado atual
    def setRegraGeradora(self, regra):
        self.regraGeradora = regra
    
    #Retorna a regra geradora do estado atual
    def getRegraGeradora(self):
        return self.regraGeradora
    
    #Seta o pai
    def setPai(self, no):
        self.pai = no
    
    #Retorna o pai
    def getPai(self):
        return self.pai
    
    #Seta o filho
    def setFilho(self, filho):
        self.filhos.append(filho)
      
    #Retorna o filho
    def getFilhos(self):
        return self.filhos
#------------------------------------------------------------------------------------------

#Classe que representa as transições do problema-------------------------------------------
class Transicoes:
    
    '''Construtor da classe inicia o mapa de transições 
    tanto no sentido horário (proximos) quanto no anti-horário (anteriores)'''
    def __init__(self): 
        #Define as transições para as quais os cavalos podem se mover (ex: da 1 para a 8)
        self.proximos = {1:8, 2:7, 3:4, 4:9, 6:1, 7:6, 8:3, 9:2}
        #self.anteriores = {1:6, 2:9, 3:8, 4:3, 6:7, 7:2, 8:1, 9:4}
        
    #Retorna o proxima posição para mover o cavalo, dada sua posição atual 
    def getProximo(self, posicao):
        return self.proximos[posicao]
    
    #Retorna a posição anterior para mover o cavalo, dada sua posição atual 
    '''def getAnterior(self, posicao):
        return self.anteriores[posicao]'''
#------------------------------------------------------------------------------------------

#Classe que representa as regras do problema-----------------------------------------------
class Regras:
    
    #Controla qual regra deve executar (de acordo com parâmetro recebido)
    def aplicaRegra(self, regra, no, estados):
        if(regra == 1):
            return self.r1(no, estados)
        elif(regra == 2):
            return self.r2(no, estados)
        elif(regra == 3):
            return self.r3(no, estados)
        elif(regra == 4):
            return self.r4(no, estados)
        
    #Executa a regra 1
    def r1(self, no, estados):
        if(no.checaPosicao(0)==9): #Se o cavalo está em sua posição final, retorna falso
            return None
        else:
            noAux = no.moveCavalo(0, estados)
            if(noAux != None): #Senão, tenta mover cavalo, caso consiga, adiciona a regra e retorna verdadeiro
                no.adicionaRegra(1)
                noAux.setRegraGeradora(1)
                return noAux
            return None #Se não foi possível aplicar a regra, retorna falso
    
    #Executa a regra 2
    def r2(self, no, estados):
        if(no.checaPosicao(1)==7): #Se o cavalo está em sua posição final, retorna falso
            return None
        else:
            noAux = no.moveCavalo(1, estados)
            if(noAux != None): #Senão, tenta mover cavalo, caso consiga, adiciona a regra e retorna verdadeiro
                no.adicionaRegra(2)
                noAux.setRegraGeradora(2)
                return noAux
            return None #Se não foi possível aplicar a regra, retorna falso
    
    #Executa a regra 3
    def r3(self, no, estados):
        if(no.checaPosicao(2)==3): #Se o cavalo está em sua posição final, retorna falso
            return None
        else:
            noAux = no.moveCavalo(2, estados)
            if(noAux != None): #Senão, tenta mover cavalo, caso consiga, adiciona a regra e retorna verdadeiro
                no.adicionaRegra(3)
                noAux.setRegraGeradora(3)
                return noAux
            return None #Se não foi possível aplicar a regra, retorna falso
    
    #Executa a regra 4
    def r4(self, no, estados):
        if(no.checaPosicao(3)==1): #Se o cavalo está em sua posição final, retorna falso
            return None
        else:
            noAux = no.moveCavalo(3, estados)
            if(noAux != None): #Senão, tenta mover cavalo, caso consiga, adiciona a regra e retorna verdadeiro
                no.adicionaRegra(4)
                noAux.setRegraGeradora(4)
                return noAux
            return None #Se não foi possível aplicar a regra, retorna falso
    
#------------------------------------------------------------------------------------------

#PROGRAMA PRINCIPAL------------------------------------------------------------------------
estadoInicial = [1,3,7,9]
estadoFinal = [9,7,3,1]

arquivo = open('Largura.txt', 'w') #Abre arquivo para escrita

t = Transicoes() #Instancia um objeto da classe de Transições
controle = Regras() #Instancia um controlador da classe Regras

listaDeAbertos = [] #Cria a lista de abertos vazia
listaDeFechados = [] #Cria a lista de fechados vazia

n = No(0) #Cria nó raiz
n.setEstado(estadoInicial) #Seta seu estado com o inicial
listaDeAbertos.append(deepcopy(n)) #Adiciona na lista de abertos
estados = []
estados.append(estadoInicial)
estadoAtual = n #Estado atual é a raiz
fracasso = False

#LOOP PRINCIPAL

inicio = time.time() #Inicia a contagem de tempo

#Enquanto não chega no estado final ou fracasso, executa a busca em largura
while(estadoAtual.getEstado() != estadoFinal):
           
    for r in range (1,5,1): #Testa todas as regras possíveis (de r1 até r4)
        noAux = controle.aplicaRegra(r, estadoAtual, estados) #Tenta aplicar regra e retorna o nó gerado ou None
        if(noAux != None): #Se gerou um nó, adiciona este na lista de abertos
            estados.append(noAux.getEstado())
            listaDeAbertos.append(deepcopy(noAux))
    
    if(len(listaDeAbertos) >= 1):
        listaDeFechados.append(listaDeAbertos.pop(0))
        
    if(len(listaDeAbertos) >= 1):
        estadoAtual = listaDeAbertos[0] #O estado atual recebe o primeiro da lista (na ordem em que foram gerados)
    else:
        arquivo.write("Fracasso")
        fracasso = True
        break
    
fim = time.time() #Finaliza a contagem de tempo


#IMPRIMINDO A SOLUÇÃO
arquivo.write("\nLista de Abertos: \n")
for l in range(0, len(listaDeAbertos), 1):
    arquivo.write(str(listaDeAbertos[l].getEstado()) + ", ")

arquivo.write("\nLista de Fechados: \n")
for l in range(0, len(listaDeFechados), 1):
    arquivo.write(str(listaDeFechados[l].getEstado()) + ", ")

if(not fracasso):
    arquivo.write("\n\nSolução de nível: " + str(estadoAtual.getNivel()) + "\n")
    
    caminhoSolucao = []
    caminhoSolucao.append(estadoAtual.getEstado())
    regras = []
    regras.append(estadoAtual.getRegraGeradora()) 
    pai = estadoAtual.getPai() 
    while(pai != None):
        caminhoSolucao.insert(0, pai.getEstado())
        regras.insert(0, pai.getRegraGeradora()) 
        pai = pai.getPai()
        
    arquivo.write("Regras|Caminho: \n" )
    arquivo.write("EI => " + str(caminhoSolucao[0]) + "\n")
    for i in range(1, len(caminhoSolucao), 1):
        arquivo.write("R" + str(regras[i]) + " => " + str(caminhoSolucao[i]) + "\n")
    
    arquivo.write("Tempo de execução: " + str(fim - inicio))
    arquivo.close()
