import os
import pandas as pd 

#Verifica se Pasta Existe
def transformaCSVExcel(arquivo):

    #Abre o Arquivo para Leitura
    read_file = pd.read_csv(arquivo  + '.csv', sep=';',encoding='latin-1',index_col=False)

    #Salva o Arquivo Novamente
    read_file.to_excel(arquivo  + '.xlsx', index = None, header=True)

    #Exclui o Arquivo CSV da pasta para Manter somente o Novo Arquivo
    os.remove(arquivo  + '.csv')