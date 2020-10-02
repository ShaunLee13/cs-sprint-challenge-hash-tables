def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # base case; if there's only one item in the length of our list, its invalid
    if length <= 1:
        return None

    weight_cache = {}

    for ind, val in enumerate(weights):
        # this will store the weight as the key and the value will be the index as a list
        # if weight already exists, it will just append the index to the end of the list at that index
        if val in weight_cache:
            weight_cache[val].append(ind)
        else:
            weight_cache[val] = [ind]

    for item in weight_cache:
        # now that we have keys we can search through, we can compare them to the limit
        if limit - item in weight_cache:
            # limit - item will give us the remaining weight to search for
            # first check that the index where l-i is not where i is at
            if weight_cache[limit - item] is weight_cache[item]:
                # and if that is where we are looking, then check the length
                # if theres more than one item in the list, then we've found our match
                if len(weight_cache[item]) > 1:
                    # and we will return the index 1 and 0 at items location, highest index first
                    return (weight_cache[item][1], weight_cache[item][0])
            # if our limit - item is not the same weight as our first, we'll return the 0 index of both of those, higher index first
            else:
                return (weight_cache[limit - item][0], weight_cache[item][0])
    # and if there's not two items that match, return None in the end
    return None
