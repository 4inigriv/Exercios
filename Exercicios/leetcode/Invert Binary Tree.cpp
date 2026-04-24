struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
};
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr)
            return nullptr;
//troca dos filhos usando uma variavel auxliar 
        TreeNode* temp = root->left;
        root->left  = root->right;
        root->right = temp;
// de forma recursiva pros outros filhos
        invertTree(root->left);  
        invertTree(root->right);

        return root;
    }
};
