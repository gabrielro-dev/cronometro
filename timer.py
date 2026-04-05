#Cronometro
import time

horas = 0
minutos = 0
segundos = 0

cont = 0
while True:
    if cont == 0:
       segundos += 1
       print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
       time.sleep(1)
       if segundos == 59:
          segundos = segundos - 59
          minutos += 1
          if segundos == 0:
             print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
             time.sleep(1)
             if minutos == 59:
                minutos = minutos - 59
                horas += 1
                print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
                time.sleep(1)
