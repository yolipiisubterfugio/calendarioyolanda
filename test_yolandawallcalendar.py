from yolanda_wall_calendar import wall_calendar

def test_crear_calendario_fecha_valida():
    
    wall_calendar()
    
    date = wall_calendar(1989, 11, 13)
    

    date_str = str(date)
    

    assert date_str == "Lunes, 13 de noviembre de 1989"

