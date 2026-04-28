struct Node {
    int val;
    Node* next;
};
void inserir_no_final(Node*& head, int value) {
    Node* novo = new Node();
    novo->val  = value;
    novo->next = nullptr;

    Node* atual = head;

    while (atual->next != nullptr) {  // enquanto next não for null, anda
        atual = atual->next;
    }
    // saiu do while: atual->next É nullptr, chegamos no último

    atual->next = novo;   // último aponta pro novo
    novo->next  = nullptr; // novo aponta pro null
}