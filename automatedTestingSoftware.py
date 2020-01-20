from random import randint, choice
import datetime
import string
from placaEcuador import *

n=0
nmax=100 #change this value to increment the number of tests
rules=["antigua","nueva"] #if you want just one rule, eliminate one them

while(n<=nmax):

    #initialize random variables
    yy=randint(1980, 2100)
    mm=randint(1, 12)
    dd=randint(1, 31)
    hours=randint(0, 23)
    hours="{0:0=2d}".format(hours)
    minutes=randint(0, 59)
    minutes="{0:0=2d}".format(minutes)
    time=hours+":"+minutes
    placaInt=randint(0, 9999)
    placaInt="{0:0=4d}".format(placaInt)
    placaString=choice(string.ascii_letters)+choice(string.ascii_letters)+choice(string.ascii_letters)
    rule=choice(rules)

    #try / except statement to avoid non valid plates or dates
    try:

        #initialize objects date and PlacaEcuador
        myPlaca=PlacaEcuador(placaString+placaInt)
        day=datetime.datetime(yy, mm, dd, 0, 0, 0, 0)

        #convert dd-mm-yy to a date string in the right format
        dd="{0:0=2d}".format(dd)
        mm="{0:0=2d}".format(mm)
        yy="{0:0=2d}".format(yy)
        date=dd + "-" + mm + "-" + yy

        #day of the week cases
        dayOfTheWeek = {
            1: "Lunes",
            2: "Martes",
            3: "Miércoles",
            4: "Jueves",
            5: "Viernes",
            6: "Sábado",
            7: "Domingo"
        }

        #print important information
        print("placa = " + myPlaca.placaString+myPlaca.placaInt)
        print("day of the week = " + dayOfTheWeek.get(day.weekday()+1))
        print("date = " + date)
        print("time = " + time)

        #test
        if myPlaca.canBeOnTheRoad(date,time,rule):
            print("El vehículo SÍ puede conducir en el rango de fecha y hora indicado, usando las leyes de tránsito " + rule.lower() + "s\n")
        else:
            print("El vehículo NO puede conducir en el rango de fecha y hora indicado, usando las leyes de tránsito " + rule.lower() + "s\n")
        n+=1
    except:
        pass

