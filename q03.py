'''
Q03
Escreva um programa que leia uma sequência de números inteiros e 
insira-os em uma fila até que um número negativo seja digitado. 
Em seguida, remova todos os elementos da fila e 
exiba-os na ordem em que foram inseridos.
'''
from fila import Fila # usar a classe Fila do arquivo fila.py

# Criar interação com o usuário
print("Programa para inserir números inteiros em uma fila")
print("Digite um número negativo para sair")
novafila = Fila()
while True:
    valor = int(input("Digite um número: "))
    if valor < 0:
        break
    novafila.inserir(valor)
    
# Mostrar números na ordem em que foram inseridos
# Só precisa mostrar a própria fila
print("Números na ordem em que foram inseridos:")
novafila.mostrar()