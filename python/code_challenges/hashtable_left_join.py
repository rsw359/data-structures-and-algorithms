from data_structures.hashtable import Hashtable


def left_join(table1, table2):
    output = []
    for key in table1:
        join_left = [key, table1.get(key), table2.get(key)]
        output.append(join_left)
    return output

# def left_join(table1, table2):
#     output = []
#     ht = Hashtable()
#     for key in table1:
#         ht.set(table1.key, table1.value)
#         if ht.contains(table1.key) and ht.contains(table2.key):
#             join_left = ht.set(table2.key, table2.value)
#         output.append(join_left)
#     return output

