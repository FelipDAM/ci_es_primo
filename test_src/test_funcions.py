'''gay'''
import src.funcions as es_primo

def test_primo_1():
    '''Tamare es un import'''
    assert es_primo.es_primo(1) is False

def test_es_primo_numero_primo():
    '''Tamare es un import'''
    assert es_primo.es_primo(2) is True

def test_es_primo_negativo():
    '''Tamare es un import'''
    assert es_primo.es_primo(-10) is False


def test_es_primo_numero_primo_mayor_2():
    '''Tamare es un import'''
    assert es_primo.es_primo(29) is True
