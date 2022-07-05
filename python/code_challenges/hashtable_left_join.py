from data_structures.hashtable import Hashtable


def left_join(table1, table2):
    output = []
    for key in table1:
        join_left = [key, table1.get(key), table2.get(key)]
        output.append(join_left)
    return output



