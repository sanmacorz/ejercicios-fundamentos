#!/usr/bin/env python3
# Calcular el gasto de agua de una vivienda tomando en cuenta la cantidad de metros cubicos gastados, a partir del sistema de cobro.

cuota_fija = 10000
metros_gastados = int(input("Ingrese la cantidad de metros de agua gastados: "))

if metros_gastados <= 50:
    costo_total = cuota_fija
elif metros_gastados < 200 and metros_gastados > 50:
    costo_total = (metros_gastados - 50) * 2000 + cuota_fija
else:
    costo_total = (metros_gastados - 50) * 3000 + cuota_fija
    
print("El costo total es de " + str(costo_total) + " pesos.")