#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # weights = []
    # length = int
    # limit = int
    """
    YOUR CODE HERE
    """
    for i in range(length):
        if hash_table_retrieve(ht, weights[i]):
            hash_table_retrieve(ht, weights[i])['quantity'] += 1
            hash_table_retrieve(ht, weights[i])['index'] = i
        else:
            hash_table_insert(ht, weights[i], { 'quantity': 1, 'index': i })
        if not hash_table_retrieve(ht, limit - weights[i]):
            hash_table_insert(ht, limit - weights[i], { 'quantity': 0 })

    for i in range(length):
        difference = limit - weights[i]
        instances = 1
        if difference == weights[i]:
            instances = 2

        pair = hash_table_retrieve(ht, difference)
        if pair and pair['quantity'] == instances:
            if i > pair['index']:
                print(i, pair['index'])
                return (i, pair['index'])
            else:
                print(pair['index'], i)
                return (pair['index'], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
