# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    table = dict()
    answer = []

    for el in files:
        if el not in table:
            table[el] = el.split("/")

    for k, v in table.items():
        for el in queries:
            if el == v[-1]:
                answer.append(k)

    return answer
