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
    
    def calcular_bonificaciones(self):
        pago_horas_extras = self.calcular_pago_horas_extras()
        movilidad = 1000
        bonificacion_suplementaria = 0.03 * self.sueldo_basico
        bonificaciones = movilidad + bonificacion_suplementaria + pago_horas_extrasfab
        return bonificaciones

    def calcular_descuentos(self):
        remuneracion_computable = self.sueldo_basico + 1000 + 0.03 * self.sueldo_basico
        descuento_faltas = remuneracion_computable / 30 * self.dias_falta
        descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * self.minutos_tardanza
        descuentos = descuento_faltas + descuento_tardanzas
        return descuentos

    def calcular_sueldo_neto(self):
        bonificaciones = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos()
        sueldo_neto = self.sueldo_basico + bonificaciones - descuentos
        return sueldo_neto

    def imprimir_boleta_pago(self):
        os.system('cls')
        sueldo_neto = self.calcular_sueldo_neto()
        print("----------BOLETA DE PAGO POR SERVICIOS----------")
        print("Fecha - Hora : ",Fecha)
        print("")
        print("Boleta de pago para      ", self.nombre_trabajador)
        print("Sueldo básico:           ", self.sueldo_basico)
        print("Horas extras trabajadas: ", self.horas_extras)
        print("Días de falta:           ", self.dias_falta)
        print("Minutos de tardanza:     ", self.minutos_tardanza)
        print("Bonificaciones:          ",bonificaciones)
        print("Descuentos    :          ",descuentos)
        print("Sueldo neto a pagar:     ",sueldo_neto)

datos = CalculadoraSueldo()
datos.imprimir_boleta_pago()






