class Dia:
    """ Inicialización: La clase debe poder inicializarse tanto con valores por defecto (1 de enero de
    1970)
    • Atributos: dia,mes,anyo,dia_semana (0 el sabado y el 6 el viernes)
    """
    def __init__(self, anyo=1970, mes=1, dia=1):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia
        self.dia_semana = self.calcular_dia_semana()

        if not self.fecha_es_valida()and self.es_bisiesto():
            raise ValueError("Fecha no válida")
#definir errores en nº de meses y días (no menos de 1)
    def fecha_es_valida(self):
        if self.mes < 1 or self.mes > 12:
            return False

        if self.dia < 1:
            return False
 # definir max dias/mes en función del mes con la excepción de feb
        dias_por_mes = {
            1: 31, 2: 29 if self.es_bisiesto() else 28,
            3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31,
            11: 30, 12: 31
        }

        return self.dia <= dias_por_mes[self.mes]
#excepción bisisestos    
    def es_bisiesto(self):
        if (self.anyo % 4 == 0 and self.anyo % 100 != 0) or (self.anyo % 400 == 0):
            return True
        else:
            return False
        
    """ Calculamos los diferentes casos para los años bisiestos, de 1970 a 2000 y de 2000 en adelante para la asignacion del dia de la semana
    """

    def calcular_dia_semana(self):
        anyo = self.anyo
        mes = self.mes

        if anyo > 2000:
            A = anyo % 100
            B = anyo // 100
            C = 2 - B + B // 4
            D = A // 4
            E = 13 * (mes + 1) // 5
            F = self.dia

            dia_semana = (A + C + D + E + F - 1) % 7
            return dia_semana

        elif anyo == 2000 and mes > 2:  # Si es el año 2000 pero el mes es posterior a febrero
            A = anyo % 100
            B = anyo // 100
            C = 2 - B + B // 4
            D = A // 4
            E = 13 * (mes + 1) // 5
            F = self.dia

            dia_semana = (A + C + D + E + F - 1) % 7
            return dia_semana

        elif self.es_bisiesto():
            A = anyo % 100
            B = anyo // 100
            C = 2 - B + B // 4
            D = A // 4
            E = 13 * (mes + 1) // 5
            F = self.dia 

            dia_semana = (A + C + D + E + F) % 7 
            return (dia_semana + 1) % 7  
            
        else:
            A = anyo % 100
            B = anyo // 100
            C = 2 - B + B // 4
            D = A // 4
            E = 13 * (mes + 1) // 5
            F = self.dia

            dia_semana = (A + C + D + E + F) % 7
            return dia_semana



mi_dia = Dia(1989, 11, 13)
mi_dia2 = Dia(2000, 2, 29)
mi_dia3 = Dia(2015, 9, 11)

print("Año:", mi_dia.anyo)
print("Mes:", mi_dia.mes)
print("Día:", mi_dia.dia)
print("Día de la semana:", mi_dia.dia_semana)

print("Año:", mi_dia2.anyo)
print("Mes:", mi_dia2.mes)
print("Día:", mi_dia2.dia)
print("Día de la semana:", mi_dia2.dia_semana)

print("Año:", mi_dia3.anyo)
print("Mes:", mi_dia3.mes)
print("Día:", mi_dia3.dia)
print("Día de la semana:", mi_dia3.dia_semana)









