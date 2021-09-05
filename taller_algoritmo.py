# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:51:46 2021

@author: Carlos Perez
"""

# Ejercicio 1


def calcularMasa(presion, vol, temp):
    
    masa = (presion * vol) / (0.37 * (temp + 460))
    
    return masa


print("Se va a calcular la masa \n")
presion = float(input("Digite la presion : \n"))
vol = float(input("Digite el volumen : \n"))
temp = float(input("Digite la temperatura : \n"))
print(f"La masa calculada es {calcularMasa(presion, vol, temp)}")


# Ejercicio 2

def calcularNumPulsaciones(edad):
    
    pulsaciones = (200 - edad) / 10
    
    return pulsaciones

print("Se va a calcular el numero de pulsaciones.")
edad = int(input("Digite su edad: \n"))
print("El numero de pulsaciones que debe tener por 10 seg es :")
print(calcularNumPulsaciones(edad))


# Ejercicio 3

def calcularPorcentaje(dinTotal, dinInver):
    
    porcentaje = (dinInver * 100) / dinTotal
    
    return porcentaje

print("Se va a calcular el porcentaje de inversion de cada persona.")
print("Persona 1")
persona1 = float(input("Digite su dinero a invertir: \n"))
print("Persona 2")
persona2 = float(input("Digite su dinero a invertir: \n"))
print("Persona 3")
persona3 = float(input("Digite su dinero a invertir: \n"))
dinTotal = persona1 + persona2 + persona3
print("El porcentaje de la Persona 1 es: ")
print(f"% {calcularPorcentaje(dinTotal, persona1)}")
print("El porcentaje de la Persona 2 es: ")
print(f"% {calcularPorcentaje(dinTotal, persona2)}")
print("El porcentaje de la Persona 3 es: ")
print(f"% {calcularPorcentaje(dinTotal, persona3)}")


# Ejercicio 4

def calcularSaldoFinal(saldoInicial):
    
    interes = (saldoInicial * 1.5) / 100
    saldoFinal = saldoInicial + interes
    
    return saldoFinal

print("Se va a calcular el saldo final con intereses de % 1.5")
saldoInicial = float(input("Digite su dinero a ahorrar: \n"))
print(f"El saldo final es : $ {calcularSaldoFinal(saldoInicial)}")


# Ejercicio 5

def calcularDescuento(salario):
    
    leyPolPub = (salario * 1) / 100
    segSocial = (salario * 4) / 100
    segForzoso = (salario * 0.5) / 100
    cajaAhorro = (salario * 5) / 100
    
    return (leyPolPub + segSocial + segForzoso + cajaAhorro)


print("Se va a calcular el salario final aplicando descuentos")
salario = float(input("Digite su salario: \n"))
salarioFinal = salario - calcularDescuento(salario)
print(f"El salario final es : $ {salarioFinal}")


# Ejercicio 6

def calcularCostoAviso(cantPalabras, cantCm, cantColores):
    
    costPalabras = cantPalabras * 20000
    costCm = cantCm * 15000
    costColor = cantColores * 25000
    
    return (costPalabras + costCm + costColor)


print("Se va a calcular el monto a paar por un aviso clasificado")
palabras = int(input("Digite cantidad de palabras: \n"))
centimetros = int(input("Digite cantidad de centimetros: \n"))
colores = int(input("Digite cantidad de colores: \n"))
print("El costo del aviso es : ")
print(f"$ {calcularCostoAviso(palabras, centimetros, colores)}")


# Ejercicio 7

def calcularBonificacion(cantAnios):
    
    bonificacion = (cantAnios * 120000) - 20000
    
    return bonificacion


print("Se va a calcular el monto a pagar por bonificaciones")
anios = int(input("Digite cantidad de años en la empresa: \n"))
print(f"El monto de bono a pagar es $ {calcularBonificacion(anios)}")


# Ejercicio 8

def calcularDescuentoProf(cantHoras):
    
    salario = 20000 * cantHoras
    descuentos = (salario * 5) / 100
    
    return salario - descuentos


print("Se va a calcular el monto a pagar al profesor")
horas = int(input("Digite cantidad de horas: \n"))
print(f"El monto a pagar es $ {calcularDescuentoProf(horas)}")


# Ejercicio 9

def calcuarCostoLlamada(montoConsum):
    
    return (montoConsum * 1.20)


print("Se va a calcular el costo total de la llamada")
monto = int(input("Digite monto consumido: \n"))
print(f"El costo de la llamada es $ {calcuarCostoLlamada(monto)}")


# Ejercicio 10

def calcularRevelado(cantFotos):
    
    revelado = cantFotos * 1500
    iva = revelado * 0.16
    
    
    return revelado + iva


print("Se va a calcular el costo total del revelado")
fotos = int(input("Digite cantidad de fotos: \n"))
print(f"El costo del revelado es $ {calcularRevelado(fotos)}")


# Ejercicio 11

def cantidad_dinero(area, dinero):
    if(area == 'Ginecologia'):
        monto = dinero * 0.4
    elif(area == 'Traumatologia'):
        monto = dinero * 0.3
    elif(area == 'Pediatria'):
        monto = dinero * 0.3
    else:
        return 0
    return monto

print("Se va a calcular el presupuesto por area")
dinero = int(input("Digite la cantidad con que cuenta el hospital: \n"))
print(f"El hospital cuenta con {dinero} pesos")
print(f"Ginecologia obtendra: $ {cantidad_dinero('Ginecologia', dinero)}")
print(f"Traumatologia obtendra {cantidad_dinero('Traumatologia', dinero)}")
print(f"Pediatria obtendra {cantidad_dinero('Pediatria', dinero)}")

# Ejercicio 12

def monto_alquiler(cant_peliculas, num_dias):
    if(cant_peliculas > 1):
        costo_peli = (cant_peliculas - 1) * 1500
    else:
        costo_peli = cant_peliculas * 1500
    costo_total = costo_peli * num_dias
    return costo_total


print("Se va a calcular el monto a pagar por alquiler")
peliculas = int(input("Digite la cantidad de peliculas a alquilar: \n"))
num_dias = int(input("Digite la cantidad de dias a alquilar: \n"))
print(f"El cliente alquilo {peliculas} peliculas.")
print(f"El cliente demoro {num_dias} dias")
print(f"El monto total a pagar es de ${monto_alquiler(peliculas, num_dias)}")

# Ejercicio 13


def familia_tour(cant_personas, cant_dias):
    costo_personas = (cant_personas * 25000) * cant_dias
    costo_iva = costo_personas * 12 / 100
    costo_total = costo_personas + costo_iva
    return costo_total


print("Se va a calcular el monto a pagar por tour")
personas = int(input("Digite la cantidad de personas: \n"))
dias = int(input("Digite la cantidad de dias: \n"))
print(f"la familia tiene {personas} miembros.")
print(f"Se van a quedar {dias} dias.")
print(f"El monto total a pagar es de ${familia_tour(personas, dias)}")

# Ejercicio 14


def pagar_habitacion(dias):
    monto = 0
    for i in range(1, dias + 1):
        if(i == 1):
            monto = monto + 100000
        else:
            monto = monto + 200000
    return monto


print("Se va a calcular el monto a pagar por habitacion")
dias = int(input("Digite la cantidad de dias: \n"))
print(f"Se van a quedar {dias} dias.")
print(f"El monto total a pagar es de ${pagar_habitacion(dias)}")

# Ejercicio 15


def monto_cuoas(monto_prest):
    mitad_prest = monto_prest * 0.5
    cuotas_esp = mitad_prest / 4
    intereses = monto_prest * 24 / 100
    cuotas_ord = mitad_prest / 20
    monto_total = monto_prest + intereses
    dic_result = {
        'monto_total': monto_total,
        'cuotas_esp': cuotas_esp,
        'cuotas_ord': cuotas_ord
        }
    return dic_result


print("Se va a calcular el monto de cuotas a pagar")
prestamo = int(input("Digite la cantidad del prestamo: \n"))
det_prest = monto_cuoas(prestamo)
print(f"Se prestaron ${prestamo}.")
print(f"El monto total a pagar es de ${det_prest['monto_total']}")
print(f"la cuota especial es de ${det_prest['cuotas_esp']} por 4 meses")
print(f"la cuota ordinaria es de ${det_prest['cuotas_ord']} por 20 meses")

