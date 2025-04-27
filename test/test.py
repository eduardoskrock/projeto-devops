import pytest
import string
import asyncio
import pytest_asyncio
import random
from unittest.mock import patch
import main

@pytest.mark.asyncio
async def test_somar():
    resultado = await main.somar(2, 3)
    assert resultado == 5

@pytest.mark.asyncio
async def test_subtrair():
    resultado = await main.subtrair(10, 4)
    assert resultado == 6

@pytest.mark.asyncio
async def test_multiplicar():
    resultado = await main.multiplicar(3, 7)
    assert resultado == 21

@pytest.mark.asyncio
async def test_dividir_normal():
    resultado = await main.dividir(8, 2)
    assert resultado == 4

@pytest.mark.asyncio
async def test_dividir_por_zero():
    resultado = await main.dividir(5, 0)
    assert resultado == "Erro: divisão por zero!"