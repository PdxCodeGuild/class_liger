# Trees

Other data structures such as lists, linked lists, stacks, or queues are linear data structures that store data sequentially.

A tree is a nonlinear hierarchical data structure that consists of nodes connected by edges.

### Tree Vocab

**Node** - A node is item that contains a value and pointers to its child nodes

**Edge** - A link between two nodes

**Root** - The topmost node in a tree

**Leaf** - Any node that has no children

<img src="https://www.sqlshack.com/wp-content/uploads/2020/07/binary-search-tree-example.png" width=800/>

## Binary Search Tree
Binary Search Tree is a node-based binary tree data structure (each node only has two children) which has the following properties:

The left subtree of a node contains only nodes with values less than the node’s value.
    
The right subtree of a node contains only nodes with values greater than the node’s value.

The left and right subtree each must also be a binary search tree.



<img src="https://media.geeksforgeeks.org/wp-content/uploads/BSTSearch.png" width=400/>

## Trie

The word "Trie" is an excerpt from the word "retrieval". Trie is a sorted tree-based data-structure that stores the set of strings.

### Properties of a Trie:

The root node of the trie always represents the null node.

Each child of nodes is sorted alphabetically.

Each node can have a maximum of 26 children (A to Z).

Each node (except the root) can store one letter of the alphabet.

The following Trie diagram is storing the words ball, bat, bear, bell, bore, stack, stock and stot

<img src="https://static.javatpoint.com/ds/images/trie-data-structure.png" width=600/>


