'''
Q04
Escreva um programa que leia uma frase do usuário e 
verifique se ela é um palíndromo 
(ou seja, pode ser lida da mesma forma tanto da esquerda para a direita
quanto da direita para a esquerda). 
Utilize uma fila para armazenar os caracteres da frase.
'''

from fila import Fila # usar a classe Fila do arquivo fila.py

frase = input("Digite uma frase: ")
frase = frase.lower() # converter para minúsculas

# Criar filas
frase_invertida = Fila()

# Inverter a frase
for i in range(len(frase), 0, -1):
    frase_invertida.inserir(frase[i-1])
    
# Comparar as filas
palindromo = frase == str(frase_invertida)

# Exibir o resultado
print("Frase original: ", frase)
print("Frase invertida: ", str(frase_invertida))
print("É palíndromo? ", palindromo)