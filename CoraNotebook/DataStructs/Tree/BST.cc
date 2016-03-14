#include <iostream>
using namespace std;

struct Node {
	int val;
	Node *left;
	Node *right;
};

void bstInit(Node*& root) {
	root = NULL;
}

// Pass root in by reference since value of root can change
// in the function in the case where the tree is empty
// (Root refers to original variable passed in, instead of it being copied)
void insert(Node*& root, int item) {
	if (root == NULL) {
		root = new Node();
		root->val = item;
		root->left = NULL;
		root->right = NULL;
		return;
	}

	if (item < root->val) {
		insert(root->left, item);
	} else if (item > root->val) {
		insert(root->right, item);
	} 
}

int countNodes(Node *root) {
	if (root == NULL) {
		return 0;
	}

	int count = 1; 	// count root
	count += countNodes(root->left);
	count += countNodes(root->right);
	return count;
}

// left, root, right
void inOrder(Node *root) {
	if (root != NULL) {
		inOrder(root->left);
		cout << root->val << endl;
		inOrder(root->right);return;
	}
}

// left, right, root
void postOrder(Node *root) {
	if (root != NULL) {
		postOrder(root->left);
		postOrder(root->right);
		cout << root->val << endl;
	}
}

// root, left, right
void preOrder(Node *root) {
	if(root != NULL) {
		cout << root->val << endl;
		preOrder(root->left);
		preOrder(root->right);
	}
}

bool has(Node *root, int item) {
	if (root == NULL) {
		return false;
	} else if (root->val == item) {
		return true;
	} else if (item < root->val) {
		return has(root->left, item);
	} else {
		return has(root->right, item);
	}
}

void deleteItem(Node* root, int item) {
	if (root == NULL) {return;}
	Node *curr = root;
	Node *parent = NULL;

	// assumes item is in tree
	while(curr != NULL && curr->val != item) {
		if (item < curr->val) {
			parent = curr;
			curr = curr->left;
		} else {
			parent = curr;
			curr = curr->right;
		}
	}

	if (curr->left == NULL && curr->right == NULL) { 		// Case 0: no children
		if (parent == NULL) {
			root = NULL;
		} else if (parent->left == curr) {
			parent->left = NULL;
		} else {
			parent->right = NULL;
		}
		delete(curr);
	} else if (curr->left == NULL && curr->right != NULL) {	// Case 1: 1 child
		if (parent == NULL) {
			root = curr->right;
		} else if (parent->left == curr) {
			parent->left = curr->right;
		} else {
			parent->right = curr->right;
		}
		delete(curr);
	} else if (curr->left != NULL && curr->right == NULL) {
		if (parent == NULL) {
			root = curr->left;
		} else if (parent->left == curr) {
			parent->left = curr->left;
		} else {
			parent->right = curr->left;
		}
		delete(curr);
	} else if (curr->left != NULL && curr->right != NULL) { // Case 2: 2 children
		// find max in left subtree
		// max in left subtree wil never have 2 subtrees
		// because largest value will not have a right subtree
		Node *max = curr->left;
		Node *prevMax = curr;
		while (max->right != NULL) {
			prevMax = max;
			max = max->right;
		}

		curr->val = max->val;
		if (prevMax == curr) {
			prevMax->left = max->left;
		} else {
			prevMax->right = curr->left;
		}
		delete(max);
	}
}

int main() {
	Node *tree;
	bstInit(tree);
	insert(tree, 5);
	insert(tree, 4);
	insert(tree, 7);
	insert(tree, 2);
	insert(tree, 3);
	insert(tree, 6);
	insert(tree, 1);

	// inOrder(tree); 	// 1 2 3 4 5 6 7
	// preOrder(tree);	// 5 4 2 1 3 7 6
	// postOrder(tree);	// 1 3 2 4 6 7 5

	cout << countNodes(tree) << " nodes" << endl;

	int find = 9;
	if (has(tree, find)) {
		cout << "Tree has " << find << endl;
	} else {
		cout << "Tree doesn't have " << find << endl;
	}

	deleteItem(tree, 7);
	inOrder(tree);

	return 0;
}
