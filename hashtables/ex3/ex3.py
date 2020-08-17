def intersection(arrays):
    """
    YOUR CODE HERE
    """

    table = dict()
    answer = []

    for lst in arrays:
        for num in lst:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
    for k, v in table.items():
        if v == len(arrays):
            answer.append(k)

    return answer


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
print(intersection([[2, 4, 7, 3], [98, 53, 2, 67], [12, 32, 2, 3]]))
