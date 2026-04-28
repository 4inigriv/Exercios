#INSERIR NO FINAL 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def inserir_no_final(self, value):
    novo = Node(value)
    novo.next = None
    atual = self.head

    while atual.next is not None:  # enquanto next não for None, anda
        atual = atual.next
    # saiu do while: atual.next É None, chegamos no último

    atual.next = novo   # último aponta pro novo
    novo.next  = None   # novo aponta pro None