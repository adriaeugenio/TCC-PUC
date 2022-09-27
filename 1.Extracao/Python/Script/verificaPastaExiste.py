import os

#Verifica se Pasta Existe
def verificaPasta(caminho):

    if os.path.isdir(caminho):

        tmp = ""

    else: 

        os.makedirs(caminho)  