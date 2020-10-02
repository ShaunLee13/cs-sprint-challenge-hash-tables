def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    nums = {}

    #we first want to loop through the a list we are getting
    # so we can save them to our nums dict
    for num in a:
        nums[num] = num

    # for each number in our dict, we'll get the negative number to check for
    for num in nums:
        check = 0 - num

        # if that number is negative and if it is in our dict, then we can add our current num to the result list
        if check < 0 and check in nums:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
