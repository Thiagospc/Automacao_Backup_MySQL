# importações usadas
import os
from datetime import datetime

# databases do banco
databases = ['sigepro2', 'sigepro', 'estatistica', 'DIEF_COMP', 'emp_atos_legais_vigentes', 'phpmyadmin', 'power_bi', 'replicacao', 'sigea_db', 'sigepro3', 'sigeproE']
now = datetime.now() # pegando data e hora atual
data_atual = now.strftime("%d_%m_%Y_%H_%M")

print("iniciando backup")
for i in databases: # loop de backup de toas as databases selecioandas
    print("%s" % (i))
    os.system("mysqldump -h IPDOSEUHOST -u SEUUSUÁRIOAQUI -pSUASENHAAQUI --routines --triggers %s > C:\\xampp\\mysql\\bin\\backup\\%s_backup_%s.sql" % (i, i, data_atual))
    print(" %s finalizado" % (i))
print("backup terminado do host 172.0.0.1 completo.")
input('clique enter para sair!')





