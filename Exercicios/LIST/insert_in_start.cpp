
#include <iostream>
struct Node {
    int key;      
    Node* next;   
};

int main() {
    int n = 5; 
    
    Node* p = nullptr; 
    
    while (n > 0) {
        Node* q = new Node(); 
        q->next = p;          
        p = q;                
        
        q->key = n;           
        n = n - 1;            
    }
    
    // --- PARTE NOVA: Para imprimir e provar que ficou 1, 2, 3, 4, 5 ---
    Node* atual = p;
    std::cout << "A lista final ficou assim: ";
    while (atual != nullptr) {
        std::cout << atual->key << " -> ";
        atual = atual->next;
    }
    std::cout << "NIL" << std::endl;

    return 0; // Fim do programa
}