'''
Q01
Implemente uma fila simples e as operações básicas: 
    inserir, remover e mostrar o elemento da frente.
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
            self.tamanho += 1    
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
            
# Testando implementação da fila
novafila = Fila()
novafila.inserir(1)
novafila.inserir(8)
novafila.inserir(3)
novafila.inserir(5)
novafila.inserir(0)
print("Fila:", end= " ")
novafila.mostrar()
print("Primeiro elemento: ", novafila.frente())
print("Removendo elemento...", novafila.remover())
print("Fila:", end= " ")
novafila.mostrar()
print("Primeiro elemento atual:", novafila.frente())
print("Inserindo elemento 12...")
novafila.inserir(12)
print("Fila:", end= " ")
novafila.mostrar()
print("Primeiro elemento atual:", novafila.frente())