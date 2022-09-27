from os import listdir
from os.path import isfile, join
import parametros as p 
import os
import pandas as pd

#Juntas as Planilha que foram Extraidas Separadas
def juntaPlanilhas(pastaOrigem,nomeArquivo,headerList):

     #Diretorio
     diretorio =  p.pastaDados + '/' + pastaOrigem

     #Lista Adiciona o Campo 'Tabela' para os dados
     headerList.append('Tabela')

     #Lista Adiciona o Campo 'ID' para os dados
     headerList.append('ID')

     # Recupera lista de ficheiros CSV em um diretorio
     ficheiros = [f for f in listdir(diretorio) if (isfile(join(diretorio, f)) and not f.endswith('Geral.csv'))]

     #Abre ficheiro de saida...
     saida = open(diretorio + "/" + nomeArquivo + ".csv", "a" )

     for a in ficheiros:

          #Define o Caminho de Pasta
          os.chdir(p.pastaDados + '/' + pastaOrigem)

          arquivo = ficheiros[0]

          if a != arquivo:

               df = pd.read_csv(a,sep= ';',encoding='latin-1',on_bad_lines='skip')

               df.to_csv(a, sep=';',index=None, header=False,  encoding='utf-8-sig')
               
     #Define para cada ficheiro
     for f in ficheiros:

          #Define o Caminho de Pasta
          os.chdir(p.pastaDados + '/' + pastaOrigem)

          #Abre o ficheiro
          csv = open(f)

          tabela = f

          contador = 0

          #Para cada uma das demais linhas no ficheiro
          for linha in csv:

               contador += 1

               linha = linha.rstrip() + ';' + str(tabela) + ';' + str(contador) + '\n'

               saida.write(linha)

          #Fecha ficheiro CSV de entrada
          csv.close()

     for a in ficheiros:

          #Define o Caminho de Pasta
          os.chdir(p.pastaDados + '/' + pastaOrigem)

          os.remove(a)

     #Carrega de Novo Para Corrigir o Cabeçario
     df = pd.read_csv(nomeArquivo + ".csv", sep= ';',encoding='latin-1',on_bad_lines='skip')

     df.to_csv(nomeArquivo + ".csv", sep=';',index=None, header=headerList,  encoding='utf-8-sig')            