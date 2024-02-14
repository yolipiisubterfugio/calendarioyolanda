class Dia:
    def __init__(self, anyo=1970, mes=1, dia=1):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia
        self.dia_semana = self.calcular_dia_semana()

        if not self.fecha_es_valida():
            raise ValueError("Fecha no válida")

    def fecha_es_valida(self):
        if self.mes < 1 or self.mes > 12:
            return False

        dias_por_mes = {
            1: 31, 2: 29 if self.es_bisiesto() else 28,
            3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31,
            11: 30, 12: 31
        }

        return 1 <= self.dia <= dias_por_mes[self.mes]

    def es_bisiesto(self):
        if self.anyo % 4 != 0:
            return False
        elif self.anyo % 100 != 0:
            return True
        elif self.anyo % 400 != 0:
            return False
        else:
            return True

    def calcular_dia_semana(self):
        if self.mes < 3:
            self.anyo -= 1
            self.mes += 12

        A = self.anyo % 100
        B = self.anyo // 100
        C = 2 - B + B // 4
        D = A // 4
        E = 13 * (self.mes + 1) // 5
        F = A + C + D + E + self.dia - 1

        return F % 7

mi_dia = Dia(1989, 11, 13)


print("Año:", mi_dia.anyo)
print("Mes:", mi_dia.mes)
print("Día:", mi_dia.dia)
print("Día de la semana:", mi_dia.dia_semana)


