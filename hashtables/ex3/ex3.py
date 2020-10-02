def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # nums is our cache. result is a list of all items that are in all arrays
    nums = {}
    result = []

    # we start by looping through each array so we can get down to the individual numbers
    for arr in arrays:
        for num in arr:
            # for each number in each array, if the numbers not in there, we'll make a slot for it. 
            # otherwise we'll iterate it by one
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1

    # now that we've looped over all numbers and gotten counts,
    # we can check if the counter at each number is equal to the length of our arrays.
    # if it is, we know its in all of the arrays and can add it to our result list
    for num in nums.keys():
        if nums[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
