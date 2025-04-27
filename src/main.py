from fastapi import FastAPI
import random

app = FastAPI()
# main.py
async def somar(a, b):
    return a + b


async def subtrair(a, b):
    return a - b


async def multiplicar(a, b):
    return a * b


async def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


async def main():
    print("Calculadora Simples")
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números.")
        return

    if escolha == '1':
        resultado = await somar(num1, num2)
    elif escolha == '2':
        resultado = await subtrair(num1, num2)
    elif escolha == '3':
        resultado = await multiplicar(num1, num2)
    elif escolha == '4':
        resultado = await dividir(num1, num2)
    else:
        print("Opção inválida!")
        return

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
