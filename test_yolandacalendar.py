from yolanda_calendar import Dia

def test_crear_dia_con_fecha_valida():
    dia = Dia(1970, 1, 1)
    
    Dia()
    
    assert dia.anyo == 1970
    assert dia.mes == 1
    assert dia.dia == 1

def test_crear_dia_con_fecha_invalida():
    dia = Dia(1969, 15, 32)
    
    Dia()

    assert dia.anyo == False
    assert dia.mes == False
    assert dia.dia == False
    

def test_crear_dia_con_fecha_bisiesta():
    dia = Dia(2000, 2, 29)
    
    Dia()
    
    assert dia.anyo == 2000
    assert dia.mes == 2
    assert dia.dia == 29






