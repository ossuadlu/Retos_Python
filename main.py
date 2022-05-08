
from classes.Ciclista import Ciclista



print("..........................")
print("........competidores......")
print("1. registrar ciclista: ")
print("0. salir: ")
print("..........................")

Opcion=1

while(opcion!=0):
    opcion=int(input("bienvenido digite una opcion: "))
    if(opcion==1):
        nombre=input("digite nombre  ciclista: ")
        edad=int(input("digite edad del ciclista: "))
        pais=("digite pais del ciclista: ")
        tiempo= int (input("digite cuantos minutos duro el recorrido del ciclista: "))
        
    ciclista=Ciclista(nombre, edad, pais, tiempo)
    menorTiempo=ciclista.calcularMenorTiempo()

print(menorTiempo)



