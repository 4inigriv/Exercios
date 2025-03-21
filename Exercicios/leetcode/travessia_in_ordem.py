
#94. Binary Tree Inorder Traversal
#Given the root of a binary tree, return the inorder traversal of its nodes' values.

#Input: root = [1,null,2,3]
#Output: [1,3,2]
#arvore simples q o pai sempre fica entre os filhos ent a ordem de colocar eles na pilha deve ser filho esquerdo,pai,fiho direito

class Solution(object):
    def inorderTraversal(self, root): #root é tipo nó 
        if root is None: # no = null
            return [] # null
        r = self.inorderTraversal(root.left)  # visita filho esquerdo
        r.append(root.val)  # visita nó pai
        r.extend(self.inorderTraversal(root.right))  # visita filho direito
        return r
