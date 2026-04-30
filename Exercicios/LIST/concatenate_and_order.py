class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
def merge(L1, L2):
    d = Node(0)
    C = d
    while L1 and L2:          
        if L1.val <= L2.val:   
            C.next = L1
            L1 = L1.next
        else:
            C.next = L2
            L2 = L2.next
        C = C.next   #encadeia diretoo resto            
    return d.next              

# função auxiliar pra imprimir a lista
def print_list(node):
    while node:
        print(node.val, end=" → ")
        node = node.next
    print("None")

# monta a lista 1: 1 → 2 → 4
L1 = Node(1)
L1.next = Node(2)
L1.next.next = Node(4)

# monta a lista 2: 1 → 3 → 4
L2 = Node(1)
L2.next = Node(3)
L2.next.next = Node(4)

# testa
resultado = merge(L1, L2)
print_list(resultado)
# esperado: 1 → 1 → 2 → 3 → 4 → 4 → None
#file:///C:/Users/virgi/Downloads/merge_linked_lists_interactive.html caso eu esqueça como eh