import os
#EMPRESA HORIZONTE -- RESOLUCION EXAMEN PARCIAL

class CalculadoraSueldo:
    def __init__(self):
        self.nombre_trabajador = input("Ingrese el nombre del trabajador: ")
        self.sueldo_basico = float(input("Ingrese el sueldo básico del trabajador: "))
        self.horas_extras = int(input("Ingrese las horas extras trabajadas: "))
        self.dias_falta = int(input("Ingrese los días de falta del trabajador: "))
        self.minutos_tardanza = int(input("Ingrese los minutos de tardanza del trabajador: "))

    def calcular_pago_horas_extras(self):
        pago_hora_normal = self.sueldo_basico / 30 / 8
        pago_horas_extras = 1.5 * pago_hora_normal * self.horas_extras
        return pago_horas_extras

    





