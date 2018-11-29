class RBNode:


 def __init__(self, key, parent, is_red=False, left=None, right=None):
 	self.key = key[0]
    self.embedding = key[1:]
    self.left = left
    self.right = right
    self.parent = parent

	if is_red:
    	self.color = "red"
    else:
        self.color = "black"

def are_both_children_black(self):
	if self.left != None and self.left.is_red():
    	return False
        if self.right != None and self.right.is_red():
        	return False
        	return True 

def count(self):
	count = 1
    if self.left != None:
    	count = count + self.left.count()
    if self.right != None:
    	count = count + self.right.count()
        return count

def get_grandparent(self):
	if self.parent is None:
    	return None
        return self.parent.parent

def get_predecessor(self):
	node = self.left
    while node.right is not None:
    	node = node.right
        return node

def get_sibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
            return self.parent.left
        return None

def get_uncle(self):
    grandparent = self.get_grandparent()
    if grandparent is None:
        return None
        if grandparent.left is self.parent:
            return grandparent.right
        return grandparent.left

def is_black(self):
	return self.color == "black"

def is_red(self):
	return self.color == "red"

def find(self, item):
    curr_RBnode = self.root
    while curr_RBnode is not None:
    	
    	if curr_RBnode.item == item:
            return curr_RBnode

        elif item < curr_RBnode.item:
            curr_RBnode = curr_RBnode.left

        else:
        	curr_RBnode = curr_RBnode.right

       	return

def replace_child(self, current_child, new_child):
	if self.left is current_child:
    	return self.set_child("left", new_child)
    elif self.right is current_child:
    	return self.set_child("right", new_child)
        return False

def set_child(self, which_child, child):
	if which_child != "left" and which_child != "right":
    	return False

   	if which_child == "left":
    	self.left = child
    else:
    	self.right = child

	if child != None:
    	child.parent = self

    return True


def get_key(self):
	return self.key

def get_embedding(self):
	return self.embedding

