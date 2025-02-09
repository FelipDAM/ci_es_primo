from src.funcions import eSPriMo

def test_primo_1():
    assert eSPriMo(1) == False

def test_es_primo_numero_primo():
    assert eSPriMo(2) == True
 
def test_es_primo_negativo():
    assert eSPriMo(-10) == False

def test_es_primo_numero_primo_mayor_2():
    assert eSPriMo(29) == True