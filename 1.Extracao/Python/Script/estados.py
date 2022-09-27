import requests
import os
import parametros as p
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(p.pastaDados + '/Estados')

#Define a Url de Origem do Arquivo
remote_url = p.urlOrigemCidadesEstados + "Lista_Estados_Brasil_Versao_CSV.csv"

#Define a Url o Local de Salvamento do Arquivo
local_file = p.pastaDados + '/Estados/' + 'Estados.csv'

#Requisição HTTP
data = requests.get(remote_url)

print(remote_url)

#Salva o Arquivo
with open(local_file, 'wb') as file:

    file.write(data.content) 

#Define o Caminho de Pasta
os.chdir(p.pastaDados + '/Estados')  

#Transforma o Arquivo CSV em Excel
ce = csvexcel.transformaCSVExcel('Estados')      