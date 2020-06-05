#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []

    for t in tickets:
            cache[t.source] = t.destination
    cur = "NONE"
    for i in range(0,length):
        route.append(cache[cur])
        cur = cache[cur]
    return route


