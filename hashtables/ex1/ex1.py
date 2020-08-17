

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    table = dict()

    for i in range(length):
        current = weights[i]
        total = (limit - current)

        if total in table:
            index = table[total]

            return (i, index)
        else:
            table[current] = i

    return None


answer_2 = get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)

print(answer_2)
