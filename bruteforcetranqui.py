#Importando recursos:

import os
import time

#Cantidad de intentos fallidos 
attempts = 15

print("Launching fake brute-force attempts...\n")

for i in range(attempts):
    print(f"[{i+1}/{attempts}] Trying invalid login...") #Imprime el proceos, es estetico
    os.system(r'net use \\127.0.0.1\IPC$ /user:fakeuser wrongpass') #Intenta acceder al recurso IPC$ del propio equipo usando credenciales fake
    time.sleep(2) #Pausa para que Windows genere logs limpios
    
print("\nDone! Check Wazuh once the manager is online ₍^. .^₎Ⳋ ")