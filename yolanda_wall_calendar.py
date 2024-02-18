from yolanda_calendar import Dia
class wall_calendar:
    def __init__(self, anio=1970, mes=1, dia=1):

        self.anyo, self.mes, self.dia = self.ajustar_fecha(anio, mes, dia)

    def mostrar_fecha(self):
        # clase Dia para extrapolar día semana 
        dia_semana = Dia(self.anyo, self.mes, self.dia).calcular_dia_semana()

        # Nombre día semana/meses
        nombres_dias = ["Sábado","Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        nombres_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

        # formato fecha
        fecha = f"{nombres_dias[dia_semana]}, {self.dia} de {nombres_meses[self.mes - 1]} de {self.anyo}"
        return fecha

    def avanza(self):
        # Avanzar un día
        self.dia += 1

        # Ajustar el mes y el año si es necesario
        dias_por_mes = {
            1: 31, 2: 29 if Dia(self.anyo).es_bisiesto() else 28,
            3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31,
            11: 30, 12: 31
        }

        if self.dia > dias_por_mes[self.mes]:
            self.dia = 1
            self.mes += 1
            if self.mes > 12:
                self.mes = 1
                self.anyo += 1

    def ajustar_fecha(self, anio, mes, dia):
        # Ajustar el número de meses y años si es necesario
        while mes > 12:
            anio += 1
            mes -= 12

        # definir max dias/mes en función del mes con la excepción de feb
        dias_maximos = {
            1: 31, 2: 29 if Dia(anio).es_bisiesto() else 28,
            3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31,
            11: 30, 12: 31
        }

        # pasar de mes
        while dia > dias_maximos[mes]:
            dia -= dias_maximos[mes]
            mes += 1
            if mes > 12:
                anio += 1
                mes = 1

        return anio, mes, dia
    
mi_dia = wall_calendar(1989, 11, 13)
mi_dia2 = wall_calendar(2000, 2, 29)
mi_dia3 = wall_calendar(2015, 9, 11)
print(mi_dia.mostrar_fecha())
print(mi_dia2.mostrar_fecha()) 
print(mi_dia3.mostrar_fecha())