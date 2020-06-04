# weights_3 = [4, 6, 10, 15, 16]
# weights_2 = [4, 4]

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    times = 0
    for i in range(0, length):
        times += 1
        print('it ran: ', times)
        weight_needed =  limit - weights[i]
        if weight_needed in cache:
            print('in cache')
            weight1 = cache[weight_needed]
            weight2 = weights[i]
            if weight1 >= weight2:
                print('first if')
                return [i, weight1]
            elif weight2 > weight1:
                return [weight1, i]

        else:
            cache[weights[i]] = i
    return None

# print(get_indices_of_item_weights(weights_3, 5, 21))
# print(get_indices_of_item_weights(weights_2, 2, 8))