import AVLTree
import RedBlackTree
import math

#Creates the AVL Tree based on user input 
def init_AVL(file, tree):
    avl_tree = tree.AVLTree()
    with open(file, encoding='UTF8') as dictionary:
        for line in dictionary:
            word = line.split(" ",1)[0]
            items = line.split()
            if word.isalpha():
                items = convert(items[1:51])
                avl_tree.insert(tree.AVLNode(word, items))
    return tree
# Creates the RB Tree based on user input 
def init_RedBlackTree(file, tree):
    rbt = tree.RedBlackTree()
    with open(file, encoding='UTF8') as file:
        for line in file:
            word = line.split(" ", 1)[0]
            items = line.split()
            if word.isalpha():
                items = convert(items[1:51])
                rbt.insert(tree.RBTNode(word, None, items))
    return tree
# This method visits the desired depth of the trees
def wordsDepth(root, new_file, d):

        if root is None:
            return
        if d < 0:
            new_file.write(root.key + "\n")
            return
        else:
            wordsDepth(root.left, new_file, d - 1)
            wordsDepth(root.right, new_file, d - 1)
            
#This method counts the number of node for each tree             
def numNodes(root):
        if root is None:
            return 0
        return 1 + numNodes(root.right) + numNodes(root.left)
 
#This method converts between strings to floats
def convert(a):
        embed = []
        size = len(a)
        for i in range(size):
            embed.append(float(a[i]))
        return embed

#This method computes heigth of the tree
def height(root):
        if root is None:
            return -1
        right = height(root.right)
        left = height(root.left)
        if left < right:
            return 1 + left
        return 1 + right
    
#This method prints the full tree     
def wordsTree(root, file):
        if root is None:
            return None
        file.write(root.item, " ")
        wordsTree(root.right)
        wordsTree(root.left)
        
#This method compares the similarities of the words with the given second file 
def compare_sim(filename, T):
    with open(filename) as support:
        for line in support:
            print(line.split()[0] + " " + line.split()[1] + " " + str(similarity(T, line.split()[0], line.split()[1])))
            
# This method computes similarity according to the given formmula
def similarity(tree, word1, word2):
    w1 = tree.find(word1)
    w2 = tree.find(word2)
    top = 0
    a = 0
    b = 0
    for i in range(len(w1.embedding)):
        num += w1.embedding[i] + w2.embedding[i]

    for i in range(len(w1.embedding)):
        den_a += w1.embedding[i] ** 2

    for i in range(len(w2.embedding)):
        den_b += w2.embedding[i] ** 2

    a = math.sqrt(a)
    b = math.sqrt(b)

    return num / (a * b)

#The main method handles the user's input and creating of the files.
def main():
       user_input = int(input("AVL Tree [0] 1. Red-Black Tree [1] "))

        if user_input == 0:
            print("AVL Tree:")
            tree = init_AVL("glove.6B.50d.txt", AVLTree)
            print("Number of nodes in tree: ", numNodes(tree.root))
            print("Height of tree:", height())
            depth = int(input("Select a depth to traverse to."))
            with open("words_at_d.txt", "w", encoding='UTF8') as file:
                wordsDepth(tree, depth, file)
            with open("wordsTree.txt", "w", encoding='UTF8') as wordsTree_file:
                wordsTree(tree, wordsTree_file)
            compare_sim("sim.txt", tree)

        if user_input == 1:
            print("Red-Black Tree:")
            tree = init_RedBlackTree("glove.6B.50d.txt", RedBlackTree)
            print("Number of nodes in tree: ", numNodes(tree.root))
            print("Height of tree:", height())
            depth = int(input("Select a depth to traverse to."))
            with open("words_at_d.txt", "w", encoding='UTF8') as file:
                wordsDepth(tree, depth, file)
            with open("wordsTree.txt", "w", encoding='UTF8') as wordsTree_file:
                wordsTree(tree, wordsTree_file)
            compare_sim("sim.txt", tree)
main()
