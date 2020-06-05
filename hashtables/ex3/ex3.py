def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    num_of_lists = len(arrays)
    result = []
    
    for l in arrays:
        for i in l:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
                if cache[i] == num_of_lists:
                    result.append(i)
    return result


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))

