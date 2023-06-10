'''
Q02
Crie um programa que exibe ao usuário um menu com as seguintes opções: 
adicionar número na fila; remover número da fila; tamanho da fila; 
mostrar fila. 
Todas as opções devem funcionar conforme a ação que ela descreve.
'''

class No:
    def __init__(self, valor):
        self.dado = valor
        self.prox = None
        
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def vazia(self):
        return self.inicio == None
        
    def inserir(self, valor):
        novo = No(valor)
        if self.inicio == None:
            self.inicio = novo
            self.fim = self.inicio
        else:
            self.fim.prox = novo # mudar o proximo do antigo fim para o novo elemento
            self.fim = novo # mudar o fim para o novo elemento
        self.tamanho += 1
            
    def remover(self):
        if self.inicio == None:
            print("Fila vazia")
        else:
            # salva o dado do inicio para retornar
            dado = self.inicio.dado
            # mudar o inicio para o proximo elemento
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None # sempre que o inicio for None, o fim também será
            self.tamanho -= 1    
            return dado # retorna o dado removido
                
    def mostrar(self):
        if self.inicio == None:
            print("Fila vazia")
        else:
            atual = self.inicio # atual recebe o inicio
            while atual != None: # enquanto atual for diferente de None, ou seja, enquanto não chegar no fim
                print(atual.dado, end = " ") # printar o dado do atual
                atual = atual.prox # atual recebe o proximo elemento
            print() # pular linha
            
    def frente(self):
        if self.inicio == None:
            print("Fila vazia")
        else:
            return self.inicio.dado # retorna o dado do inicio
            
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