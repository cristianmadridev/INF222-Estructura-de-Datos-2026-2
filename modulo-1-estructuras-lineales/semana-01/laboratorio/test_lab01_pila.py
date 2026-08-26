"""
Pruebas automáticas — Lab 1 (Pila)
Este archivo lo ejecuta el autograder por GitHub Actions en cada push
(ver .github/workflows/autograding.yml). No lo modifiques: es el mismo
criterio de corrección para todos los estudiantes.

Este archivo es el PATRÓN a seguir para escribir las pruebas de las
siguientes semanas: un test_labXX_*.py junto al lab correspondiente,
usando pytest.raises para los casos de error y asserts simples para el
resto. No hace falta que el docente escriba pruebas para las 15 semanas
antes de empezar el curso — se agregan la semana en que se asigna cada
laboratorio.
"""
import pytest
from lab01_pila import Pila


def test_pila_vacia_al_crear():
    p = Pila()
    assert p.is_empty() is True
    assert p.size() == 0


def test_push_incrementa_size():
    p = Pila()
    p.push(1)
    p.push(2)
    p.push(3)
    assert p.size() == 3
    assert p.is_empty() is False


def test_peek_no_modifica_la_pila():
    p = Pila()
    p.push(10)
    p.push(20)
    tope = p.peek()
    assert tope == 20
    assert p.size() == 2  # peek no debe eliminar


def test_pop_retorna_el_tope_lifo():
    p = Pila()
    p.push("a")
    p.push("b")
    p.push("c")
    assert p.pop() == "c"
    assert p.pop() == "b"
    assert p.size() == 1


def test_pop_en_pila_vacia_lanza_indexerror():
    p = Pila()
    with pytest.raises(IndexError):
        p.pop()


def test_peek_en_pila_vacia_lanza_indexerror():
    p = Pila()
    with pytest.raises(IndexError):
        p.peek()
