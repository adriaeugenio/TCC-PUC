from os import listdir
from os.path import isfile, join
import parametros as p 
import os
import pandas as pd

#Juntas as Planilha Extraida com o Histórico de Dados
def juntaPlanilhasHistorico(pastaOrigem,nomeArquivo):

     # Diretorio
     diretorio =  p.pastaDados + '/' + pastaOrigem

     # Recupera lista de ficheiros csv do diretorio
     ficheiros = [f for f in listdir(diretorio) if (isfile(join(diretorio, f)) and f.endswith('.csv'))]

     # Recupera lista de novos ficheiros csv do diretorio
     ficheirosNovos = [f for f in listdir(diretorio) if (isfile(join(diretorio, f)) and not f.endswith('Geral.csv'))]

     # Abre ficheiro de saida...
     saida = open(diretorio + "/" + nomeArquivo + ".csv", "a" )

     #Exclui a Linha do Cabeçario
     for a in ficheirosNovos:

          #Define o Caminho de Pasta
          os.chdir(p.pastaDados + '/' + pastaOrigem)

          df = pd.read_csv(a,sep= ';',encoding='latin-1',on_bad_lines='skip')

          df.to_csv(a, sep=';',index=None, header=False,  encoding='utf-8-sig')
               
     #Define para cada ficheiro
     for f in ficheiros:

          #Define o Caminho de Pasta
          os.chdir(p.pastaDados + '/' + pastaOrigem)

          #Abri o ficheiro
          csv = open(f)

          #Para cada uma das demais linhas no ficheiro...
          for linha in csv:

               linha = linha.rstrip() + ';' + '\n'

               saida.write(linha)

          #Fecha ficheiro CSV de entrada
          csv.close()

     for a in ficheiros:

          #Define o Caminho de Pasta
          os.chdir(p.pastaDados + '/' + pastaOrigem)

          os.remove(a)        