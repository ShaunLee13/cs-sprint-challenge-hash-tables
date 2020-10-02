#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_store = {}
    route = [None] * length

    #we want to enumerate over tickets and slot those onto our hash table
    for ticket in tickets:
        ticket_store[ticket.source] = ticket.destination
    
    #since we start at NONE, that destination will be our start
    destination = ticket_store['NONE']

    # now we iterate through the length. we will assign each index in range, starting with destination.
    # the following destination will equal the value in our ticket store, and will continue until we reach the end
    for ind in range(length):
        route[ind] = destination
        destination = ticket_store[destination]

    return route 
