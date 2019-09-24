# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:54:44 2019

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
    
    '''Construtor: inicia todas as posições de estado com 0 (vazio), cria um vetor vazio de 
    regras e o níviel é recebido como parâmetro'''
    def __init__(self, nivel): 
        self.estado = [0, 0, 0, 0] #Cada posição representa um cavalo: 0 -> branco1, 1: -> branco2, 2 -> preto1 e 3 -> preto2
        self.nivel = nivel
        self.regras = []
        
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
    
    #Retorna o elemento correspondente na posição no vetor (representa a posição que o cavalo se encontra)
    def checaPosicao(self, posicao):
        return self.estado[posicao]
    
    #Move o cavalo para a próxima posição possível (de acordo com a regra)
    def moveCavalo(self, cavalo, estados):
        t = Transicoes() #Instancia um objeto da classe que controla as transições
        posicaoAtual = self.checaPosicao(cavalo) #Acha a posição atual do cavalo
        proximaPosicao = t.getProximo(posicaoAtual) #Acha a próxima posição possível para este
        if(proximaPosicao not in self.estado): #Se posição para qual cavalo vai andar está vazia, tenta andar
            estadoAuxiliar = deepcopy(self.estado) #Copia o estado atual p/ um auxiliar
            estadoAuxiliar[cavalo] = proximaPosicao #Move o cavalo p/ a próxima posição  
            if(estadoAuxiliar not in estados): #Se o estado auxiliar gerado ainda não apareceu nos níveis acima, passa para este estado
                self.estado = deepcopy(estadoAuxiliar) #Realiza a troca de estado
                return True #Se moveu retorna verdadeiro
        return False #Se não moveu, retorna falso
    
    #Adiciona regra no vetor
    def adicionaRegra(self, regra):
        self.regras.append(regra)
        
    #Retorna as regras usadas
    def regrasUsadas(self):
        return self.regras
    
    #Remove regra do vetor
    def removeRegra(self):
        return self.regras.pop()
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
            return False
        elif(no.moveCavalo(0, estados)): #Senão, tenta mover cavalo, caso consiga, adiciona a regra e retorna verdadeiro
            no.adicionaRegra(1)
            return True
        return False #Se não foi possível aplicar a regra, retorna falso
    
    #Executa a regra 2
    def r2(self, no, estados):
        if(no.checaPosicao(1)==7): #Se o cavalo está em sua posição final, retorna falso
            return False
        elif(no.moveCavalo(1, estados)): #Senão, tenta mover cavalo, caso consiga, adiciona a regra e retorna verdadeiro
            no.adicionaRegra(2)
            return True
        return False #Se não foi possível aplicar a regra, retorna falso
    
    #Executa a regra 3
    def r3(self, no, estados):
        if(no.checaPosicao(2)==3): #Se o cavalo está em sua posição final, retorna falso
            return False
        elif(no.moveCavalo(2, estados)): #Senão, tenta mover cavalo, caso consiga, adiciona a regra e retorna verdadeiro
            no.adicionaRegra(3)
            return True
        return False #Se não foi possível aplicar a regra, retorna falso
    
    #Executa a regra 4
    def r4(self, no, estados):
        if(no.checaPosicao(3)==1): #Se o cavalo está em sua posição final, retorna falso
            return False
        elif(no.moveCavalo(3, estados)): #Senão, tenta mover cavalo, caso consiga, adiciona a regra e retorna verdadeiro
            no.adicionaRegra(4)
            return True
        return False #Se não foi possível aplicar a regra, retorna falso
#------------------------------------------------------------------------------------------

#PROGRAMA PRINCIPAL------------------------------------------------------------------------
#Define estados inicial e final do problema
estadoInicial = [1,3,7,9]
estadoFinal = [9,7,3,1]

t = Transicoes() #Instancia um objeto da classe de Transições
n = No(0) #Instancia um nó com nível inicial 0 (raiz)
controle = Regras() #Instancia um controlador da classe Regras

n.setEstado(estadoInicial) #O primeiro estado é o inicial
estados = [estadoInicial] #Adiciona esta estado no vetor de estados (caminho percorrido)
backtracking = False #Função auxiliar que indica se houve um backtracking no instante atual
fracasso = False #Função auxiliar para controlar se houve fracasso

arquivo = open('Backtracking.txt', 'w') #Abre arquivo para escrita

#LOOP PRINCIPAL

inicio = time.time() #Inicia a contagem de tempo

#Enquanto não chega no estado final ou fracasso, executa a busca Backtracking
while(estadoFinal not in estados):
    #print("Estado atual: " + str(estados[len(estados)-1]))
    if(backtracking == False): #Se ñ houve backtracking, a última regra é 0 (ainda ñ foi usada regra neste nível)
        ultimaRegra = 0
    
    temRegra = False #Variável auxiliar que controla se há regra disponível nesta iteração
    for i in range (ultimaRegra + 1,5,1): #Testa a partir da última regra (vai da última usada, até a regra 4)
        temRegra = controle.aplicaRegra(i, n, estados) #Se pode aplicar a regra em questão, a variável receberá verdadeiro
        if(temRegra): #Se aplicou, a regra, para (deve-se passar para o próximo nível)
            break
    
    if(temRegra): #Se aplicou a regra, incrementa 1 nível, e acrescenta o novo estado no caminho
        n.setNivel(n.getNivel() + 1)
        estados.append(n.getEstado())
        backtracking = False
    
    else: #Se não tem regra, deve-se realizar o backtracking
        backtracking = True
        if(len(estados) > 1): #Se o tamanho do vetor de estados é maior que 1 (A raíz tem pelo menos 1 filho)
            ultimaRegra = n.removeRegra() #Remove a última regra usada e guarda esta na variável
            ultimoEstado = estados.pop() #Remove o estado atual
            print("Backtracking, removendo estado: " + str(ultimoEstado))
            n.setEstado(estados[len(estados)-1]) #Passa para o estado do nível acima
            n.setNivel(n.getNivel() - 1) #Decrementa um nível
        else: #Se voltou até a raíz e não tem mais regra, não há solução
            arquivo.write("Não existe solução. \n")
            fracasso = True
            break
fim = time.time() #Finaliza a contagem de tempo

#IMPRIMINDO A SOLUÇÃO
#Se obteve sucesso, grava no arquivo a solução
if(not fracasso):
    arquivo.write("Solução de nível: " + str(n.getNivel()) + "\n") #Imprime o nível
    
    arquivo.write("Regras|Caminho: \n" ) #Imprime o caminho, começando pela raíz
    arquivo.write("EI => " + str(estadoInicial) + "\n")
    #Imprime as regras que levaram a cada estado, juntamente com estes estados 
    regras = n.regrasUsadas()
    for i in range (1,len(estados),1):
        e = estados[i]
        arquivo.write("R" + str(regras[i-1]) + " => " + str(e) + "\n") 

arquivo.write("Tempo de execução: " + str(fim - inicio))

arquivo.close()