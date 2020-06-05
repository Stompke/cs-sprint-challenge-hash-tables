

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in range(0, length):
        weight_needed =  limit - weights[i]
        if weight_needed in cache:
            weight1 = cache[weight_needed]
            if i > weight1:
                return [i, weight1]
            elif weight1 >= i:
                print([weight1, i])
                return [weight1, i]
        else:
            cache[weights[i]] = i
    return None
