from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    #use a set so that there are no duplicate common_values
    common_values = set()
    #create hash table
    ht = Hashtable()
    #create lists from the trees
    tree_1_values= tree1.pre_order()
    tree_2_values= tree2.pre_order()

    for value in tree_1_values:
        #set values into the hash table, must be strings
        ht.set(str(value), value)

    for value in tree_2_values:
        #check contains for the values, must be strings
        if ht.contains(str(value)):
            #add to the common list
            common_values.add(value)

    return common_values


