#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    if len(weights) < 2:
        return None

    if len(weights) == 2:
        if sum(weights) == limit:
            return (0, 1) if weights[0] > weights[1] else (1, 0)

    for i, w in enumerate(weights):
        hash_table_insert(ht, w, i)

    for w in weights:
        i1 = hash_table_retrieve(ht, w)
        i2 = hash_table_retrieve(ht, limit - w)
        if i2:
            return (i1, i2) if i1 > i2 else (i2, i1)

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
