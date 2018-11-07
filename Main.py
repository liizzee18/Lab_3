import NodeAVL
import NodeRB
import math

# (mawilliams7) Spacing across file is not uniform. Consider adopting uniform spacing.
# (mawilliams7) Consider writing function docstrings for each of your functions so it is more clear as to what you are doing
# Creates the AVL tree by reading the file and inserting the words to the tree
def AVL_tree(AVLTree):
	# (mawilliams7) I am unsure what this line is doing. Please add comment to clarify
	tree = type_of_tree.NodeAVL()
 	line = [] 
 	file = open('glove.6B.50d.txt', 'r')

 	for lines in file:
 		line = lines.split()
 		w = line[0]

 		if ignore(w):  #if the word is a character then it's ignored 
 			emmbeddings = [50] 
 			for i in range (emmbeddings.length):
 				emmbeddings[i] = line[i+1]
 			tree.insert(emmbeddings, w)  #inserts the word

	return tree

# Creates the AVL tree by reading the file and inserting the words to the tree
def RB_Tree(RBTree)

	tree = RBTree.NodeRB()
 	line = [] 
 	file = open('glove.6B.50d.txt', 'r')

 	for lines in file:
 		line = lines.split()
 		w = line[0]

 		if ignore(w):  #if the word is a character then it's ignored 
 			emmbeddings = [50] 
			# (mawilliams7) I am unsure what this code segment is doing. Consider adding comment to clarify.
 			for i in range (emmbeddings.length):
 				emmbeddings[i] = line[i+1]
 			tree.insert(emmbeddings, w)  #inserts the word

 	return tree		

# Tells apart the words from symbols 
# (mawilliams7) The logic of this function is unclear. When is the function false and when is it true?
def ignore(word):
	ascii = word[0] 
        if ascii < 97 || ascii > 122 :
            return false;        
        return true;


# Counts the nodes of the chosen tree    
def count_nodes(root):

    if root is None:
        return 0
    return 1 + count_nodes(root.right) + count_nodes(root.left)

# Computes the heigth of the chosen tree 
def height(root):
    if root is None:
        return -1
    hr = height(root.right)
    hl = height(root.left)
    if hl < hr:
        return 1 + hl
    return 1 + hr

# compares the similarities of the words in the second file
def compare(tree_):
	file3 = "similarities.tx"
    with open(file3) as support:
        for line in support:
            print(line.split()[0] + " " + line.split()[1] + " " + str(cos_similarity(tree_, line.split()[0], line.split()[1])))

def cos_similarity(tree, w0,w1):

      e0 = NodeRB.SearchWord(w0) # first word
      e1 = NodeRB.SearchWord(w1) # second word

      for i in range(50):
            dotProduct += e0[i] * e1[i]
            norm0 += math.pow(e0[i], 2)
            norm1 += math.pow(e1[i], 2)
        	square0 = math.sqrt(norm0)
       		square1 = math.sqrt(norm1)
        	cosSim = dotProduct / (square0 * square1)
        
        return cosSim
    
# Given either a AVL or RB tree a file is generated with the contained words 
def generate_file(root):
  new_file = "words_in_tree.txt"
  # (mawilliams7) Below code is incomplete
  with open("new_file", "w", encoding='UTF8') as words_in_tree_file:
            words_in_tree(red_black, words_in_tree_file

    if root is None:

        return None
    # (mawilliams7) Using recursion when writing files is not common practice. Consider using an iterative approach
    new_file.write(root.item, " ")
    generate_file(root.right)
    generate_file(root.left)


# Given either a AVL or RB tree a file is generated with the contained 
# words given at a certain depth

def generate_file_D(tree,d):

	file_depth = "words_at_d.txt"
# (mawilliams7) Same comment as above. As a matter of fact, I'm unsure of the behavior of the writer when it is writing to a file across multiple instances. This is worth looking into to improve the implementation.
with open(file_depth, "w", encoding='UTF8') as file:
            words_at_d(tree, d, file

    if root is None:
        return 
    if d < 0:
        file_depth.write(root.key + "\n")
        return
    else:
        generate_file_D(root.left,  d - 1)
       	generate_file_D(root.right, d - 1)

	
# Main method
def main():
	
	# Giving the user to choose between trees
	usr_input = int(input("1. AVL Tree\n 2. Red Black Tree\n'")
	# (mawilliams7) Fix if-elif block spacing so this code segment is more clear
		if usr_input == 1:

			tree = NodeAVL(AVLTree)
			print("Nodes in AVLTree : ", count_nodes(tree.root))
        	print("Heigth of Tree :", height(tree.root), ".")
        	print("File containing the words")
        	generate_file(tree.root)
        	d = int(input("Desired depth to view: "))
        	generate_fileD(tree.root,d)
        	print("Files similarities")
        	compare(tree)

        elif user == 2:

			tree = NodeRB(NodeRB)
			print("Nodes in RBTree : ", count_nodes(tree.root))
        	print("Heigth of Tree :", height(tree.root), ".")
        	print("File containing the words")
        	generate_file(tree.root)
        	d = int(input("Desired depth to view: "))
        	generate_fileD(tree.root,d)
        	print("Files similarities")
        	compare(tree)


			   

			


			


		 

		
