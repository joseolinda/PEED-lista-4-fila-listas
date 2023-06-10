'''
Q02
Crie um programa que exibe ao usuário um menu com as seguintes opções: 
adicionar número na fila; remover número da fila; tamanho da fila; 
mostrar fila. 
Todas as opções devem funcionar conforme a ação que ela descreve.
'''
from fila import Fila # usar a classe Fila do arquivo fila.py
            
# Criar interação com o usuário
def menu():
    print("1 - Adicionar número na fila")
    print("2 - Remover número da fila")
    print("3 - Tamanho da fila")
    print("4 - Mostrar fila")
    print("0 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

# Loop para o menu
novafila = Fila()
while True:
    opcao = menu()
    if opcao == 1:
        valor = int(input("Digite um número: "))
        novafila.inserir(valor)
        print(f"Número {valor} adicionado na fila")
    elif opcao == 2:
        removido = novafila.remover()
        if removido != None:
            print(f"Número {removido} foi removido da fila")
    elif opcao == 3:
        print(f"Tamanho da fila: {novafila.tamanho}")
    elif opcao == 4:
        print("Fila: ")
        novafila.mostrar()
    elif opcao == 0:
        print("Saindo...")
        break  # sai do loop
    else:
        print("Opção inválida")
            
    print() # pular linha