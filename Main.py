import AVLTree
import Red_Black_Tree
import pdb
import math


#This is the main method in which calls the rest of the methods
def main():

    user = input("AVL Tree [a]  Red Black Tree [r] ")
    n = user

    if user is 'a' or 'A':
        
        avl_tree = create_AVL_Tree("glove.6B.50d.txt", AVLTree)
        temp = avl_tree
        usr_output(temp,n)

    elif user is 'r':

        rb_tree = create_Red_Black_Tree("glove.6B.50d.txt", Red_Black_Tree)
        temp = rb_tree
        usr_output(temp,n)


#This method handles the printing statments along with getting the user's input 
def usr_output(tree_type , n):

    if n is 'a' or 'A':
        avl_copy = tree_type.root 

        print(" Number of Nodes : ", count_nodes(avl_copy.root))
        print("Height of Tree :", height(avl_copy.root))

        d = input("Pick a depth")         
        words_depth(avl_copy, "words_at_d.txt" , d)

        print(" Words in the tree: ")
        with open("words_in_tree.txt", "w") as file2:
            words_in_tree(avl_copy, file2)

        print("Comparing words: ")
        compare("similarities.txt", avl_tree)

    elif n is 'r' or 'R':
        rb_copy = tree_type.root

        print(" Number of Nodes : ", count_nodes(rb_copy.root))
        print("Height of Tree :", height(rb_copy.root))

        d = input("Pick a depth")        
        words_depth(rb_copy, "words_at_d.txt" , d)

        print(" Words in the tree: ")
        with open("words_in_tree.txt", "w") as file2:
            words_in_tree(rb_copy, file2)

        print("Comparing words: ")
        compare("similarities.txt", rb_copy)


# Creates the AVL Tree
def create_AVL_Tree(filename, type_of_tree):

    tree = type_of_tree.AVLTree()
    with open(filename, encoding='UTF8') as dictionary:
        for line in dictionary:
            items = line.split()
            if items.pop(0).isalpha():
                items = string_to_float(items[1:51])
                tree.insert(type_of_tree.AVLNode(items.pop(0), items))

    return tree


# Creates the RB Tree 
def create_Red_Black_Tree(filename, type_of_tree):
    tree = type_of_tree.Red_Black_Tree()

    with open(filename, encoding='UTF8') as file:
        for line in file:
            items = line.split()
            if items.pop(0).isalpha():
                items = string_to_float(items[1:51])
                tree.insert(type_of_tree.RBNode(items.pop(0), None, items))
    return tree


# Computes the height of the tree
def height(root):
    if root is None:
        return -1
    hr = height(root.right)
    hl = height(root.left)
    if hl < hr:
        return 1 + hl
    return 1 + hr

# Counts the nodes of the overall tree
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.right) + count_nodes(root.left)

#This method generates a file with all the nodes(words)
def words_in_tree(root, file):
    if root is None:
        return None

    file.write(root.item, " ")
    words_in_tree(root.right)
    words_in_tree(root.left)

#This method generates the file with the desired depth along its nodes (words)
def words_depth(x, file, d):
    f = open(file,"a")   
    if x is None:
        return
    if d == 0:       
        f.write(x.item + "\n")
    else:
        words_depth(x.left, file, d - 1)
        words_depth(x.right, file, d - 1)

#This method prints the entire tree
def print_tree(root):
    pdb.set_trace()
    if root is not None:
        if root.right is not None and root.left is not None:
            print(root.item, " ")

        print_tree(root.right)
        print_tree(root.left)


#This method handles the conversion between strings to a floats, mainly used for embeddings 
def string_to_float(holding_array):
    converted = []
    length = (len(holding_array))
    for i in range(length):
        converted.append(float(holding_array[i])) # convert to float
    # print(converted)
    return converted



# Comparing words with the given second file 
def compare(filename, T):
    with open(filename) as support:
        for line in support:
            print(line.split()[0] + " " + line.split()[1] + " " + str(similarity(T, line.split()[0], line.split()[1])))



# This method computes similarity according to the given formmula
def similarity(tree, word1, word2):
    wo1 = tree.find(word1)
    wo2 = tree.find(word2)
    top = 0
    bottom_a = 0
    bottom_b = 0
    for i in range(len(wo1.embedding)):
        top += wo1.embedding[i] + wo2.embedding[i]

    for i in range(len(wo1.embedding)):
        bottom_a += wo1.embedding[i] ** 2

    for i in range(len(wo2.embedding)):
        bottom_b += wo2.embedding[i] ** 2

    bottom_a = math.sqrt(bottom_a)
    bottom_b = math.sqrt(bottom_b)

    return top / (bottom_a * bottom_b)


main()
