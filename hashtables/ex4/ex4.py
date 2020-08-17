def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    table = dict()
    answers = []

    for el in a:
        if abs(el) not in table:
            table[abs(el)] = 1
        else:
            table[abs(el)] += 1

    for k, v in table.items():
        if v > 1:
            answers.append(k)
    return answers

# This will break in some situtations


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
