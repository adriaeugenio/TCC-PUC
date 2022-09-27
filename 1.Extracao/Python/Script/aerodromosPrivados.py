import requests
import csv
import os
import parametros as p
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(p.pastaDados + '/Aerodrómos Privados')

#Define a Url de Origem do Arquivo
remote_url = p.urlOrigem + "dadosabertos/Aerodromos/Lista%20de%20aeródromos%20privados/Aerodromos%20Privados/AerodromosPrivados.csv"

#Define a Url o Local de Salvamento do Arquivo
local_file = p.pastaDados + '/Aerodrómos Privados/' + 'AerodromosPrivados.csv'

#Requisição HTTP
data = requests.get(remote_url)

print(remote_url)

#Salva o Arquivo
with open(local_file, 'wb') as file:

    file.write(data.content)

#Define o Caminho de Pasta
os.chdir(p.pastaDados + '/Aerodrómos Privados')  

#Abre o Arquivo para Leitura
with open('AerodromosPrivados.csv', 'r', encoding='latin-1') as f:
   
   linhas = csv.reader(f, delimiter=';')
   
   linhascsv = list(linhas)

#Remove a Linha (Observação da Data de Atualização)
   linhascsv.remove(linhascsv[0])

file = open('AerodromosPrivados.csv', 'w+', newline ='') 

#Salva o Arquivo Novamente
with file: 

    write = csv.writer(file, delimiter=';') 
    write.writerows(linhascsv)

#Transforma o Arquivo CSV em Excel
ce = csvexcel.transformaCSVExcel('AerodromosPrivados')