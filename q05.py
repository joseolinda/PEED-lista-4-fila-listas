'''
Q05
Implemente uma fila circular utilizando um vetor e as operações básicas.
'''

class ListaCircular:
    def __init__(self):
        self.lista = []

    def esta_vazia(self):
        return len(self.lista) == 0

    def tamanho(self):
        return len(self.lista)

    def adicionar(self, valor):
        self.lista.append(valor)

    def remover(self, indice = 0):
        if self.esta_vazia():
            print("A lista está vazia.")
            return None
        # caso o índice seja maior que o tamanho da lista, ele é normalizado
        # pois, como é uma lista circular, o índice pode ser maior que o tamanho
        # da lista e ainda assim ser válido
        indice_normalizado = indice % self.tamanho() 
        valor_removido = self.lista.pop(indice_normalizado)
        return valor_removido

    def mostrar(self):
        if self.esta_vazia():
            print("A lista está vazia.")
        for indx, valor in enumerate(self.lista):
            prox = indx + 1 if indx < self.tamanho() - 1 else 0
            print(f"dado: {valor}, proximo: {self.lista[prox]}", )
        print()
        
        
# Testar a lista circular
lista = ListaCircular()
lista.adicionar(1)
lista.adicionar(8)
lista.adicionar(4)
lista.adicionar(7)
lista.adicionar(3)
lista.adicionar(9)
lista.remover()
lista.adicionar(11)
lista.adicionar(21)
lista.remover()
lista.adicionar(5)
lista.mostrar()