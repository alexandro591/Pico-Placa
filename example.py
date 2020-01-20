from placaEcuador import *

rule="nueva" #change "antigua" to "nueva" to use the new rules for pico y placa
#antigua = Hours: 7:00am - 9:30am / 16:00pm - 19:30
#nueva = Hours: 5:00am - 20:00pm

myPlaca=Placa("gkz0607") #a valid plate
date="23-01-2020" #format dd-mm-YY
time="20:00" #24h format

if myPlaca.canBeOnTheRoad(date,time,rule):
    print("El vehículo SÍ puede conducir en el rango de fecha y hora indicado, usando las leyes de tránsito " + rule + "s")
else:
    print("El vehículo NO puede conducir en el rango de fecha y hora indicado, usando las leyes de tránsito " + rule + "s")
