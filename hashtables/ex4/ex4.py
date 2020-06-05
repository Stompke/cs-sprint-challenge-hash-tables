def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}

    for i in a:
        if i not in cache:
            # add into cache with changing to opposite (pos or neg)
            cache[i*-1] = True
        else:
            result.append(abs(i))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
