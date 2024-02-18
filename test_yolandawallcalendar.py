from yolanda_calendar import wall_calendar

def test_crear_calendario_fecha_valida():
    date = wall_calendar(1989, 11, 13)
    
    wall_calendar()
    
    assert wall_calendar(1989, 11, 13) == "Lunes, 13 de noviembre de 1989"