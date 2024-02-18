from yolanda_wall_calendar import wall_calendar

def test_crear_calendario_fecha_valida():

    date = wall_calendar(1989, 11, 13)

    assert date == "Lunes, 13 de noviembre de 1989"


