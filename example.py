from placaEcuador import *

rule="nueva" #change "antigua" to "nueva" to use the new rules for pico y placa
#antigua = Hours: 7:00 - 9:30 / 16:00 - 19:30
#nueva = Hours: 5:00 - 20:00

myPlaca=PlacaEcuador("GKZ0607") #a valid plate
date="23-01-2020" #format dd-mm-YY
time="13:00" #24h format

#example using a rule
if myPlaca.canBeOnTheRoad(date,time,rule):
    print("El vehículo SÍ puede conducir en el rango de fecha y hora indicado, usando las leyes de tránsito " + rule.lower() + "s")
else:
    print("El vehículo NO puede conducir en el rango de fecha y hora indicado, usando las leyes de tránsito " + rule.lower() + "s")

#example using the default rule (antigua)
if myPlaca.canBeOnTheRoad(date,time):
    print("El vehículo SÍ puede conducir en el rango de fecha y hora indicado, usando las leyes de tránsito antiguas")
else:
    print("El vehículo NO puede conducir en el rango de fecha y hora indicado, usando las leyes de tránsito antiguas")
