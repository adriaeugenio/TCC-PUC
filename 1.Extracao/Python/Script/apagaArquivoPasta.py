import os
import pandas as pd 

#Verifica se Pasta Existe
def apagaArquivoPasta(caminhoPasta):

    #Verifica os Todos os Arquivos que Existem na Pasta
    for diretorio, subpastas, arquivos in os.walk(caminhoPasta):
                    
        for arquivo in arquivos:

            if len(os.path.join(arquivo)) >= 1:

                nomeArquivo = os.path.join(arquivo) 

    #Remove os arquivos da pasta
    if os.path.exists(caminhoPasta + nomeArquivo):

        os.remove(caminhoPasta + nomeArquivo) 