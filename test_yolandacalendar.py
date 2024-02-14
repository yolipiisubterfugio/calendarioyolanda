from yolanda_calendar import Dia

def test_crear_dia_con_fecha_valida():
    dia = Dia(1970, 1, 1)
    
    assert dia.anyo == 1970
    assert dia.mes == 1
    assert dia.dia == 1

def test_crear_dia_con_fecha_invalida():
    try:
        dia = Dia(1970, 4, 31)
    except ValueError as e:
        assert str(e) == "Fecha no válida"

def test_crear_dia_con_fecha_bisiesta():
    dia = Dia(2000, 2, 29)
    
    assert dia.anyo == 2000
    assert dia.mes == 2
    assert dia.dia == 29






