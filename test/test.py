from src.main import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Hello Word!"}

def test_funcaoteste():
    with patch('random.randint', return_value=123):
        result = teste()

    assert result == {"teste": True, "num_aleatorio": 123}

def test_create_estudante():
    estudante_test = Estudante(name="Lulu", curso="ADS", ativo=False)
    assert estudante_test == create_estudante(estudante_test)

def test_update_estudante_negativo():
    assert not update_estudante(-5)

def test_update_estudante_positivo():
    assert update_estudante(10)

def test_delete_estudante_negativo():
    assert not delete_estudante(-5)

def test_delete_estudante_positivo():
    assert delete_estudante(10)
