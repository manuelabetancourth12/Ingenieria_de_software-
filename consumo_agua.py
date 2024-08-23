aguaMC = float(input('Ingresa el consumo de agua en metros cúbicos: '))
tarifa = float(input('Ingresa el costo por metro cúbico de agua consumida: '))
pago = aguaMC * tarifa
print('El valor del pago por', round(aguaMC, 2),'metros cubicas es de $', int(pago), 'pesos.')