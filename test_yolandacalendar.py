from yolandacalendar import fecha_es_valida, es_bisiesto, calcular_dia_semana


def test_fecha_es_valida():
    # Casos válidos
    assert fecha_es_valida(1970, 1, 1) == True  # 1 de enero de 1970
    assert fecha_es_valida(2000, 2, 29) == True  # 29 de febrero de 2000 (año bisiesto)
    assert fecha_es_valida(2024, 2, 29) == True  # 29 de febrero de 2024 (año bisiesto)
    assert fecha_es_valida(2023, 12, 31) == True  # 31 de diciembre de 2023

    # Casos inválidos
    assert fecha_es_valida(1970, 4, 31) == False  # 31 de abril de 1970 (mes con 30 días)
    assert fecha_es_valida(2001, 2, 29) == False  # 29 de febrero de 2001 (no es año bisiesto)
    assert fecha_es_valida(1900, 2, 29) == False  # 29 de febrero de 1900 (no es año bisiesto)
    assert fecha_es_valida(2023, 2, 30) == False  # 30 de febrero de 2023 (mes con 28 días)
    
def test_es_bisiesto():
    # Años bisiestos
    assert es_bisiesto(2000) == True
    assert es_bisiesto(2004) == True
    assert es_bisiesto(2020) == True
    assert es_bisiesto(2400) == True

    # Años no bisiestos
    assert es_bisiesto(1900) == False
    assert es_bisiesto(2003) == False
    assert es_bisiesto(2100) == False



def test_calcular_dia_semana():
    # Ejemplos conocidos
    assert calcular_dia_semana(1970, 1, 1) == 4  # 1 de enero de 1970 (jueves)
    assert calcular_dia_semana(2023, 12, 31) == 1  # 31 de diciembre de 2023 (domingo)
    assert calcular_dia_semana(2000, 2, 29) == 2  # 29 de febrero de 2000 (martes, año bisiesto)
    assert calcular_dia_semana(2023, 2, 28) == 2  # 28 de febrero de 2023 (miércoles, año no bisiesto)


